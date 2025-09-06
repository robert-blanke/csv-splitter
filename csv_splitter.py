import pandas as pd
import argparse
import math
import os
import shutil

def split_csv(input_file, parts, output_prefix="part"):

    # Path to the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")

    # Remove output directory if it exists, then recreate it
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Read the CSV file
    df = pd.read_csv(input_file, sep=";")

    # Number of rows per part
    rows_per_part = math.ceil(len(df) / parts)

    # Create the output files
    for i in range(parts):
        start = i * rows_per_part
        end = start + rows_per_part
        df_part = df.iloc[start:end]

        output_file = os.path.join(output_dir, f"{output_prefix}_{i+1}.csv")
        df_part.to_csv(output_file, index=False, sep=";")
        print(f"Written: {output_file} with {len(df_part)} rows")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file into multiple smaller files")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("parts", type=int, help="Number of output files")
    parser.add_argument("--output-prefix", default="part", help="Prefix for output files")

    args = parser.parse_args()
    split_csv(args.input_file, args.parts, args.output_prefix)
