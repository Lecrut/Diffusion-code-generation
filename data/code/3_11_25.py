import argparse
import os

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def batch_convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line_number, line in enumerate(input_file, start=1):
                try:
                    celsius = float(line.strip())
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    output_file.write(f"{fahrenheit}\n")
                except ValueError:
                    print(f"Error processing line {line_number}: Invalid temperature value '{line.strip()}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except IOError as e:
        print(f"IO Error: {e}")

if __name__ == '__main__':
    input_data = """25.0
                    -10.0
                    37.5
                    abc"""
    input_file_path = 'temp_input.txt'
    output_file_path = 'temp_output.txt'

    with open(input_file_path, 'w') as temp_input:
        temp_input.write(input_data)

    batch_convert_temperatures(input_file_path, output_file_path)

    with open(output_file_path, 'r') as temp_output:
        print(temp_output.read())