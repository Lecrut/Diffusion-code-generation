import argparse
import sys
import os

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_temperature_file(input_path):
    results = []
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The input file '{input_path}' does not exist.")
    
    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
    except IOError as e:
        raise IOError(f"Error reading file '{input_path}': {e}")
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            celsius = float(line)
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            results.append((celsius, fahrenheit))
        except ValueError:
            results.append((line, f"Error: Invalid temperature value on line {i}"))
    
    return results

def create_arg_parser():
    parser = argparse.ArgumentParser(description="Convert temperature data from Celsius to Fahrenheit.")
    parser.add_argument('--input', type=str, help='Path to the input file containing Celsius temperatures.')
    return parser

def run_cli(args=None):
    parser = create_arg_parser()
    parsed_args = parser.parse_args(args)
    
    if parsed_args.input:
        try:
            results = process_temperature_file(parsed_args.input)
            for celsius, fahrenheit in results:
                print(f"{celsius} -> {fahrenheit}")
            return results
        except (FileNotFoundError, IOError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return None
    else:
        print("Error: --input argument is required.", file=sys.stderr)
        return None

if __name__ == '__main__':
    import tempfile
    
    sample_celsius_values = [20.0, 30.0, -40.0, 100.0]
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        for value in sample_celsius_values:
            temp_file.write(f"{value}\n")
        temp_file_path = temp_file.name
    
    try:
        results = process_temperature_file(temp_file_path)
        for celsius, fahrenheit in results:
            print(f"{celsius} C = {fahrenheit} F")
    finally:
        os.unlink(temp_file_path)