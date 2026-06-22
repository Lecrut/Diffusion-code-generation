import argparse
import csv
import io
import os
import sys

def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description='Batch convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the input CSV file containing Celsius temperatures.'
    )
    parser.add_argument(
        'output_file',
        type=str,
        help='Path to the output CSV file to write the converted Fahrenheit temperatures.'
    )
    return parser.parse_args(args)

def convert_celsius_to_fahrenheit(celsius_value):
    if not isinstance(celsius_value, (int, float)):
        raise ValueError(f"Expected a numeric value for Celsius, got {type(celsius_value).__name__}.")
    return (celsius_value * 9 / 5) + 32

def read_csv_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")
    
    rows = []
    header = None
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError(f"Input file '{file_path}' is empty.")
        
        if not header:
            raise ValueError(f"Input file '{file_path}' has no header.")
            
        for row in reader:
            if not row:
                continue
            rows.append(row)
            
    return header, rows

def process_temperature_data(header, rows):
    if not header:
        raise ValueError("Header cannot be empty.")
        
    celsius_index = -1
    for i, col_name in enumerate(header):
        if col_name.strip().lower() == 'celsius':
            celsius_index = i
            break
            
    if celsius_index == -1:
        raise ValueError("Input CSV must contain a column named 'Celsius'.")
        
    converted_rows = []
    converted_header = [col for col in header]
    converted_header.append('Fahrenheit')
    
    for row in rows:
        if len(row) <= celsius_index:
            raise ValueError(f"Row has insufficient columns. Expected at least {celsius_index + 1}, got {len(row)}.")
            
        celsius_val = row[celsius_index]
        try:
            temp_c = float(celsius_val)
        except ValueError:
            raise ValueError(f"Invalid Celsius value '{celsius_val}' in row: {row}")
            
        temp_f = convert_celsius_to_fahrenheit(temp_c)
        new_row = list(row)
        new_row.append(f"{temp_f:.2f}")
        converted_rows.append(new_row)
        
    return converted_header, converted_rows

def write_csv_data(file_path, header, rows):
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    input_path = 'input_temps.csv'
    output_path = 'output_temps.csv'
    
    import tempfile
    
    temp_input_fd, temp_input_path = tempfile.mkstemp(suffix='.csv')
    try:
        with os.fdopen(temp_input_fd, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Celsius', 'Location'])
            writer.writerow([0, 'Freezing'])
            writer.writerow([100, 'Boiling'])
            writer.writerow([37, 'Body'])
            
        args = [temp_input_path, output_path]
        parsed_args = parse_arguments(args)
        
        header, rows = read_csv_data(parsed_args.input_file)
        conv_header, conv_rows = process_temperature_data(header, rows)
        write_csv_data(parsed_args.output_file, conv_header, conv_rows)
        
        with open(parsed_args.output_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            result = list(reader)
            
        for row in result:
            print(row)
            
    finally:
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    main()