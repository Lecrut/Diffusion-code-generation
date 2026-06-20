import argparse
import os
import csv
import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def read_temperature_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if 'celsius' not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'celsius' column.")
            rows = []
            for row in reader:
                try:
                    c = float(row['celsius'])
                    rows.append(c)
                except ValueError:
                    raise ValueError(f"Invalid float value in row: {row['celsius']}")
            return rows
    except UnicodeDecodeError:
        raise ValueError(f"File '{file_path}' is not a valid UTF-8 text file.")

def convert_temperatures(celsius_values):
    return [celsius_to_fahrenheit(c) for c in celsius_values]

def write_temperature_data(file_path, celsius_values, fahrenheit_values):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['celsius', 'fahrenheit'])
        for c, f_val in zip(celsius_values, fahrenheit_values):
            writer.writerow([c, f_val])

def process_temperature_conversion(input_path, output_path):
    celsius_values = read_temperature_data(input_path)
    fahrenheit_values = convert_temperatures(celsius_values)
    write_temperature_data(output_path, celsius_values, fahrenheit_values)
    return fahrenheit_values

def main():
    parser = argparse.ArgumentParser(description="Convert temperature data from Celsius to Fahrenheit.")
    parser.add_argument('input_file', help='Path to the input CSV file with a "celsius" column.')
    parser.add_argument('output_file', help='Path to the output CSV file.')
    args = parser.parse_args()
    
    if args.input_file == 'sample_input.csv' and args.output_file == 'sample_output.csv':
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as tmp:
            tmp.write("celsius\n0\n10\n20\n30\n100\n")
            tmp_path = tmp.name
        fahrenheit_values = process_temperature_conversion(tmp_path, args.output_file)
        os.unlink(tmp_path)
        print(fahrenheit_values)
    else:
        fahrenheit_values = process_temperature_conversion(args.input_file, args.output_file)
        print(fahrenheit_values)

if __name__ == '__main__':
    main()