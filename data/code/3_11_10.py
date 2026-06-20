import argparse
import os
import sys

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', type=str, help='Path to the input file containing temperature data in Celsius.')
    return parser.parse_args(args)

def convert_celsius_to_fahrenheit(celsius_value):
    return celsius_value * 9 / 5 + 32

def process_temperature_file(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f'Input file not found: {input_path}')
    results = []
    try:
        with open(input_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    celsius_val = float(line)
                    fahrenheit_val = convert_celsius_to_fahrenheit(celsius_val)
                    results.append((celsius_val, fahrenheit_val))
                except ValueError:
                    raise ValueError(f"Invalid temperature data at line {line_num}: '{line}'. Expected a float.")
    except PermissionError:
        raise PermissionError(f'Permission denied to read file: {input_path}')
    return results

def format_results(results):
    output_lines = []
    for celsius, fahrenheit in results:
        output_lines.append(f'{celsius:.2f} C = {fahrenheit:.2f} F')
    return output_lines

def run_conversion(input_file_path):
    results = process_temperature_file(input_file_path)
    formatted = format_results(results)
    return formatted
if __name__ == '__main__':
    temp_input_content = ['0', '100', '37', '-40', '25.5']
    temp_filename = 'temp_input_celsius.txt'
    try:
        with open(temp_filename, 'w') as f:
            for val in temp_input_content:
                f.write(val + '\n')
        result_lines = run_conversion(temp_filename)
        for line in result_lines:
            print(line)
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)