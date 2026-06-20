import argparse
import json
import os
import csv

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C' and to_unit == 'F':
        return value * 9 / 5 + 32
    if from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5 / 9
    raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

def process_file(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found.")
    
    with open(input_path, 'r', newline='') as f:
        if input_path.endswith('.json'):
            data = json.load(f)
            if isinstance(data, dict):
                results = {k: convert_temperature(v, 'C', 'F') for k, v in data.items()}
                return results
            if isinstance(data, list):
                results = [convert_temperature(v, 'C', 'F') for v in data]
                return results
        
        elif input_path.endswith('.csv'):
            data = []
            reader = csv.reader(f)
            for row in reader:
                converted_row = [convert_temperature(float(val), 'C', 'F') for val in row]
                data.append(converted_row)
            return data
        else:
            raise ValueError(f"Unsupported file format: {input_path}")

def main():
    parser = argparse.ArgumentParser(description='Batch convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', type=str, help='Path to the input file (JSON or CSV).')
    args = parser.parse_args(['sample.json'])
    
    try:
        result = process_file(args.input_file)
        print(result)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()