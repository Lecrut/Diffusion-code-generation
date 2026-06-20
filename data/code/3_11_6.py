import argparse
import csv
import os
import sys

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def read_temperature_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    if not file_path.lower().endswith('.csv'):
        raise ValueError(f"The file '{file_path}' must be a CSV file.")
    
    data = []
    with open(file_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        if 'celsius' not in reader.fieldnames:
            raise ValueError("The CSV file must contain a column named 'celsius'.")
        
        for row in reader:
            try:
                celsius_val = float(row['celsius'])
                fahrenheit_val = celsius_to_fahrenheit(celsius_val)
                data.append({
                    'celsius': celsius_val,
                    'fahrenheit': fahrenheit_val
                })
            except ValueError:
                raise ValueError(f"Invalid numeric value in 'celsius' column: '{row['celsius']}'.")
    
    return data

def process_and_print_results(file_path):
    data = read_temperature_data(file_path)
    
    results = []
    for record in data:
        results.append({
            'input': record['celsius'],
            'output': record['fahrenheit']
        })
        
    for record in results:
        print(f"{record['input']} Celsius = {record['output']} Fahrenheit")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', help='Path to the input CSV file containing a "celsius" column.')
    args = parser.parse_args()
    
    try:
        process_and_print_results(args.input_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()