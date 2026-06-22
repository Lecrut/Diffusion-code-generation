import argparse
import re
import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def convert_file_to_fahrenheit(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)

    pattern = r'(-?\d+(?:\.\d+)?\s*°C)'

    def replace_temp(match):
        temp_str = match.group(1).replace('°C', '').strip()
        try:
            celsius = float(temp_str)
            fahrenheit = celsius_to_fahrenheit(celsius)
            return f"{fahrenheit:.2f}°F"
        except ValueError:
            return match.group(0)

    converted_content = re.sub(pattern, replace_temp, content)
    return converted_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Celsius to Fahrenheit in a file.")
    parser.add_argument('file_path', type=str, help="Path to the input file.")
    args = parser.parse_args()

    result = convert_file_to_fahrenheit(args.file_path)
    print(result)