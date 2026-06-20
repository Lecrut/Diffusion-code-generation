import argparse
import sys
import os
import csv

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9.0 / 5.0) + 32.0

def convert_temperature_data(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return False

    try:
        with open(input_path, 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)

            try:
                celsius_index = header.index('Celsius')
            except ValueError:
                print("Error: CSV must contain a 'Celsius' column.")
                return False

            rows = []
            for row in reader:
                try:
                    celsius_val = float(row[celsius_index])
                    fahrenheit_val = celsius_to_fahrenheit(celsius_val)
                    new_row = row[:]
                    new_row[celsius_index] = fahrenheit_val
                    rows.append(new_row)
                except (ValueError, IndexError) as e:
                    print(f"Warning: Skipping invalid row: {e}")
                    continue

        with open(output_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(rows)

        print(f"Successfully converted data to '{output_path}'.")
        return True

    except IOError as e:
        print(f"Error: Could not process file. {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit in a CSV file.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    args = parser.parse_args(['data.csv', 'result.csv'])

    sample_header = ['Temperature', 'Celsius', 'Unit']
    sample_rows = [
        ['Cold', 0, 'C'],
        ['Room Temp', 25, 'C'],
        ['Hot', 100, 'C']
    ]

    with open(args.input_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(sample_header)
        writer.writerows(sample_rows)

    success = convert_temperature_data(args.input_file, args.output_file)

    if success:
        with open(args.output_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            results = list(reader)
            for row in results:
                print(row)
    else:
        print("Conversion failed.")

    os.remove(args.input_file)
    os.remove(args.output_file)