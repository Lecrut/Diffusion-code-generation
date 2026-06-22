import argparse
import re
import sys
import tempfile
import os

def convert_temperatures_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_celsius(match):
        value = float(match.group(1))
        fahrenheit = (value * 9/5) + 32
        return f"{fahrenheit:.2f}°F"
    
    pattern = r'(-?\d+(?:\.\d+)?)°C'
    new_content = re.sub(pattern, replace_celsius, content)
    return new_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    args = parser.parse_args(['sample.txt'])
    
    sample_content = "The temperature is 20°C today. It might drop to -5°C tonight. High of 25°C expected."
    
    with open(args.file_path, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    
    try:
        result = convert_temperatures_in_file(args.file_path)
        print(result)
    finally:
        if os.path.exists(args.file_path):
            os.remove(args.file_path)