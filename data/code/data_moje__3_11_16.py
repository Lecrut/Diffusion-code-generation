import argparse
import os
import sys

def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', help='Path to the input file containing Celsius temperatures.')
    return parser.parse_args(args)

def read_temperatures(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Input file '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except IOError as e:
        print(f"Error: Could not read file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)
    temperatures = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            temp = float(line)
            temperatures.append(temp)
        except ValueError:
            print(f"Warning: Skipping non-numeric value '{line}'.", file=sys.stderr)
    return temperatures

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def convert_temperatures(temperatures):
    return [celsius_to_fahrenheit(t) for t in temperatures]

def write_temperatures(file_path, fahrenheit_temps):
    try:
        with open(file_path, 'w') as file:
            for temp in fahrenheit_temps:
                file.write(f"{temp}\n")
    except IOError as e:
        print(f"Error: Could not write to file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    args = parse_arguments(['input.csv', 'output.csv'])
    temperatures = read_temperatures(args.input_file)
    if not temperatures:
        print("Warning: No valid temperatures found in the input file.", file=sys.stderr)
        sys.exit(0)
    fahrenheit_temps = convert_temperatures(temperatures)
    write_temperatures(args.input_file.replace('.csv', '_fahrenheit.csv') if args.input_file.endswith('.csv') else args.input_file + '_fahrenheit.csv', fahrenheit_temps)
    print("Conversion complete. Results written to output file.")

if __name__ == '__main__':
    main()