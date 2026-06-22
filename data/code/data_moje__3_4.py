import re
import sys
import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

def convert_temperatures_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return None
    except IOError:
        return None

    pattern = r'(-?\d+(?:\.\d+)?)°C|(-?\d+(?:\.\d+)?)C(?!\w)'

    def replacer(match):
        if match.group(1) is not None:
            celsius = float(match.group(1))
        else:
            celsius = float(match.group(2))
        fahrenheit = celsius_to_fahrenheit(celsius)
        formatted = f"{fahrenheit:.2f}"
        return f"{formatted}°F"

    converted_content = re.sub(pattern, replacer, content)
    return converted_content

def main():
    parser = argparse.ArgumentParser(description='Convert temperatures from Celsius to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the file containing Celsius temperatures.')
    args = parser.parse_args()

    result = convert_temperatures_in_file(args.file_path)
    print(result)

if __name__ == '__main__':
    import os
    import tempfile
    sample_content = "The temperature is 25°C today and yesterday it was -4.5C."
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(sample_content)
        temp_file_path = f.name
    try:
        result = convert_temperatures_in_file(temp_file_path)
        print(result)
    finally:
        os.unlink(temp_file_path)