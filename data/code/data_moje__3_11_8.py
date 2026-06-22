import argparse
import tempfile
import os

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32.0

def process_temperature_file(input_path):
    results = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = float(stripped)
                fahrenheit = convert_celsius_to_fahrenheit(value)
                results.append({
                    'line': line_num,
                    'celsius': value,
                    'fahrenheit': fahrenheit
                })
            except ValueError:
                raise ValueError(f"Invalid temperature data on line {line_num}: '{stripped}'")
    return results

def main():
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', help='Path to the input file containing Celsius temperatures')
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File not found: {args.input_file}")
        return
    
    try:
        output_data = process_temperature_file(args.input_file)
        for item in output_data:
            print(f"Line {item['line']}: {item['celsius']}C -> {item['fahrenheit']}F")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_data = "25.0\n-10.5\n0.0\n100.0"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(sample_data)
        tmp_file_path = tmp_file.name
    
    try:
        temp_data = process_temperature_file(tmp_file_path)
        for item in temp_data:
            print(f"Line {item['line']}: {item['celsius']}C -> {item['fahrenheit']}F")
    finally:
        os.remove(tmp_file_path)