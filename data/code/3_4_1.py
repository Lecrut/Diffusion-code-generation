import argparse
import sys

def convert_temperatures(content):
    import re

    def celsius_to_fahrenheit(match):
        temp_str = match.group(1)
        celsius = float(temp_str)
        fahrenheit = celsius * 9 / 5 + 32
        if fahrenheit == int(fahrenheit):
            formatted = str(int(fahrenheit))
        else:
            formatted = f'{fahrenheit:.1f}'
            if '.' in formatted:
                formatted = formatted.rstrip('0').rstrip('.')
        return f'{temp_str}F'
    pattern = '(-?\\d+(?:\\.\\d+)?)\\s*[Cc]'
    converted_content = re.sub(pattern, celsius_to_fahrenheit, content)
    return converted_content

def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return convert_temperatures(content)
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."

def create_parser():
    parser = argparse.ArgumentParser(description='Convert Celsius temperatures to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the input file containing Celsius temperatures.')
    return parser
if __name__ == '__main__':

    def main():
        parser = create_parser()
        sample_file_path = 'sample_temps.txt'
        sample_content = 'Temperature: 0C\nAnother temp: 100.5C\nCold day: -40C'
        with open(sample_file_path, 'w') as f:
            f.write(sample_content)
        result = process_file(sample_file_path)
        print(result)
        import os
        if os.path.exists(sample_file_path):
            os.remove(sample_file_path)
    main()