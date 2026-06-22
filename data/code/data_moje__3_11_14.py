import argparse
import csv
import sys
import os

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def process_temperature_file(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    
    results = []
    try:
        with open(input_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            if 'celsius' not in reader.fieldnames:
                raise ValueError("Input CSV must contain a 'celsius' column.")
            
            for row in reader:
                try:
                    c_val = float(row['celsius'])
                    f_val = celsius_to_fahrenheit(c_val)
                    results.append({'celsius': c_val, 'fahrenheit': f_val})
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Invalid temperature value in row: {row}.") from e
    except PermissionError:
        raise PermissionError(f"Permission denied reading '{input_path}'.")
    
    if not results:
        raise ValueError("No data rows found in input file.")
    
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['celsius', 'fahrenheit']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert temperature data from Celsius to Fahrenheit.")
    parser.add_argument('--input_file', default='temp_input.csv', help='Path to input CSV file.')
    parser.add_argument('--output_file', default='temp_output.csv', help='Path to output CSV file.')
    
    args = parser.parse_args([])
    
    sample_celsius_data = "celsius\n0\n100\n25\n-40\n37\n"
    with open(args.input_file, 'w', encoding='utf-8') as f:
        f.write(sample_celsius_data)
    
    converted_data = process_temperature_file(args.input_file, args.output_file)
    
    for item in converted_data:
        print(item)