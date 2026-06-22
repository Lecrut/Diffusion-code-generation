import argparse
import sys
import os

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32

def process_temperature_file(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    results = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                celsius = float(line)
                fahrenheit = convert_celsius_to_fahrenheit(celsius)
                results.append(f"{celsius:.2f} C -> {fahrenheit:.2f} F")
            except ValueError:
                raise ValueError(f"Invalid numeric value on line {line_num}: '{line}'")
    
    return results

def create_parser():
    parser = argparse.ArgumentParser(description="Batch convert Celsius to Fahrenheit from a file.")
    parser.add_argument('input_file', type=str, help='Path to the input file containing Celsius values')
    return parser

def main():
    parser = create_parser()
    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(1)
    
    try:
        output_lines = process_temperature_file(args.input_file)
        for line in output_lines:
            print(line)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    import tempfile
    sample_data = "20\n-5\n0\n100\n37.5"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(sample_data)
        temp_path = tmp_file.name
    
    try:
        results = process_temperature_file(temp_path)
        for res in results:
            print(res)
    finally:
        os.unlink(temp_path)