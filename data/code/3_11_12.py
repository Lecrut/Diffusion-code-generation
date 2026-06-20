import argparse
import csv
import io
import sys

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def convert_temperature_file(input_path, output_path):
    try:
        with open(input_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            if reader.fieldnames is None:
                raise ValueError("Input file is empty or has no header.")
            if 'celsius' not in reader.fieldnames:
                raise ValueError("Input CSV must contain a 'celsius' column.")
            
            rows = []
            for row in reader:
                raw_val = row['celsius'].strip()
                if not raw_val:
                    continue
                try:
                    val = float(raw_val)
                except ValueError:
                    raise ValueError(f"Invalid numeric value in celsius column: '{row['celsius']}'")
                
                f_val = celsius_to_fahrenheit(val)
                row['fahrenheit'] = f_val
                rows.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {input_path}")
    except Exception as e:
        raise RuntimeError(f"Error processing file: {e}")

    header = None
    if rows:
        header = list(rows[0].keys())
    
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    
    return len(rows)

def main():
    parser = argparse.ArgumentParser(description='Batch convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', help='Path to input CSV file')
    parser.add_argument('output_file', help='Path to output CSV file')
    args = parser.parse_args()

    count = convert_temperature_file(args.input_file, args.output_file)
    print(count)

if __name__ == '__main__':
    main()