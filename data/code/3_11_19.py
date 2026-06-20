import argparse
import sys
import os
import tempfile
import json
import math

def convert_celsius_to_fahrenheit(celsius_value):
    return celsius_value * 9 / 5 + 32

def process_temperature_file(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except Exception as e:
        raise IOError(f"Error reading input file: {e}")
    
    if not lines:
        raise ValueError("Input file is empty")
    
    results = []
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        
        try:
            value = float(line)
            if math.isnan(value) or math.isinf(value):
                raise ValueError(f"Invalid numeric value at line {line_num}")
            converted = convert_celsius_to_fahrenheit(value)
            results.append({
                "original": value,
                "converted": converted,
                "line": line_num
            })
        except ValueError:
            raise ValueError(f"Invalid temperature value at line {line_num}: {line}")
    
    if not results:
        raise ValueError("No valid temperature data found in input file")
    
    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for result in results:
                outfile.write(f"{result['converted']:.2f}\n")
    except Exception as e:
        raise IOError(f"Error writing output file: {e}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Batch convert temperature data from Celsius to Fahrenheit')
    parser.add_argument('--input', required=False, help='Input file path containing Celsius values')
    parser.add_argument('--output', required=False, help='Output file path for Fahrenheit values')
    
    args = parser.parse_args()
    
    if args.input is None or args.output is None:
        temp_input = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_input.write("0\n100\n37.5\n-273.15\n")
        temp_input.close()
        
        temp_output = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
        temp_output.close()
        
        input_path = temp_input.name
        output_path = temp_output.name
    else:
        input_path = args.input
        output_path = args.output
    
    if not os.path.exists(input_path):
        temp_input = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_input.write("0\n100\n37.5\n-273.15\n")
        temp_input.close()
        input_path = temp_input.name
    
    try:
        results = process_temperature_file(input_path, output_path)
        print(json.dumps(results, indent=2))
    finally:
        if 'temp_input' in locals() and os.path.exists(input_path):
            os.remove(input_path)
        if 'temp_output' in locals() and os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    main()