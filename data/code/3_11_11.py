import argparse
import csv
import os
import sys

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_file(input_path, output_path):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    results = []

    with open(input_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader, None)
        if header is None:
            raise ValueError("Input file is empty or has no data rows.")

        for row in reader:
            if len(row) != 2:
                raise ValueError(f"Invalid row format: {row}")
            try:
                temp_c = float(row[1])
                temp_f = celsius_to_fahrenheit(temp_c)
                results.append([row[0], temp_f])
            except ValueError:
                raise ValueError(f"Invalid temperature value: {row[1]}")

    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([header[0], "Fahrenheit"])
        writer.writerows(results)

    return results

def main():
    parser = argparse.ArgumentParser(description="Convert temperature data from Celsius to Fahrenheit.")
    parser.add_argument('input_file', help="Path to the input CSV file.")
    parser.add_argument('output_file', help="Path to the output CSV file.")
    args = parser.parse_args()

    try:
        results = convert_file(args.input_file, args.output_file)
        print(results[0])
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("City,Celsius\n")
        f.write("New York,10\n")
        f.write("London,15\n")
        temp_in = f.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        temp_out = f.name

    import sys
    sys.argv = ['test_script', temp_in, temp_out]
    main()

    os.unlink(temp_in)
    os.unlink(temp_out)