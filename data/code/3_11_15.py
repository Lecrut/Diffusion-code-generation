import argparse
import csv
import sys
import tempfile
import os
from pathlib import Path

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def parse_temperature_csv(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    
    results = []
    with open(input_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        if 'celsius' not in reader.fieldnames:
            raise ValueError("Input CSV must contain a 'celsius' column.")
        
        for row_index, row in enumerate(reader, start=2):
            raw_val = row['celsius'].strip()
            if not raw_val:
                raise ValueError(f"Empty temperature value at row {row_index}.")
            try:
                celsius_val = float(raw_val)
            except ValueError:
                raise ValueError(f"Non-numeric temperature value '{raw_val}' at row {row_index}.")
            
            fahrenheit_val = celsius_to_fahrenheit(celsius_val)
            results.append({
                'original_celsius': celsius_val,
                'converted_fahrenheit': fahrenheit_val
            })
            
    if not results:
        raise ValueError("Input CSV contains no data rows.")
        
    return results

def format_conversion_results(results):
    output_lines = []
    output_lines.append("Celsius to Fahrenheit Conversion Results:")
    output_lines.append("-" * 40)
    
    for item in results:
        c = item['original_celsius']
        f = item['converted_fahrenheit']
        output_lines.append(f"Celsius: {c:6.2f} => Fahrenheit: {f:6.2f}")
        
    output_lines.append("-" * 40)
    output_lines.append(f"Total rows processed: {len(results)}")
    
    return "\n".join(output_lines)

def convert_temperature_file(input_path):
    results = parse_temperature_csv(input_path)
    output = format_conversion_results(results)
    return output

def main():
    parser = argparse.ArgumentParser(description="Batch convert temperature data from Celsius to Fahrenheit.")
    parser.add_argument('input_file', help="Path to the input CSV file containing a 'celsius' column.")
    args = parser.parse_args()
    
    try:
        result_output = convert_temperature_file(args.input_file)
        print(result_output)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    
    sample_csv_content = """celsius
0
100
25
-40"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as tmp_file:
        tmp_file.write(sample_csv_content)
        tmp_file_path = tmp_file.name
    
    try:
        result_output = convert_temperature_file(tmp_file_path)
        print(result_output)
    finally:
        os.unlink(tmp_file_path)