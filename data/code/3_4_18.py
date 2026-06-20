import argparse
import re
import os
import tempfile

TEMPERATURE_PATTERN = r'(-?\d+(?:\.\d+)?)\s*C\b'

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32.0

def convert_file_temperatures(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer(match):
        celsius_value = float(match.group(1))
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        if fahrenheit_value == int(fahrenheit_value):
            return f"{int(fahrenheit_value)}F"
        return f"{fahrenheit_value:.1f}F"
    
    converted_content = re.sub(TEMPERATURE_PATTERN, replacer, content)
    return converted_content

class TemperatureConverter:
    def __init__(self):
        self.conversions = []
    
    def process_text(self, text):
        lines = text.splitlines()
        processed_lines = []
        for line in lines:
            converted_line = self._convert_line(line)
            processed_lines.append(converted_line)
            if converted_line != line:
                self.conversions.append(converted_line)
        return '\n'.join(processed_lines)
    
    def _convert_line(self, line):
        def replacer(match):
            celsius_value = float(match.group(1))
            fahrenheit_value = celsius_to_fahrenheit(celsius_value)
            if fahrenheit_value == int(fahrenheit_value):
                return f"{int(fahrenheit_value)}F"
            return f"{fahrenheit_value:.1f}F"
        return re.sub(TEMPERATURE_PATTERN, replacer, line)

def main():
    parser = argparse.ArgumentParser(description='Convert Celsius temperatures in a file to Fahrenheit.')
    parser.add_argument('file_path', help='Path to the input file')
    args = parser.parse_args(['temp_data.txt'])
    
    with open(args.file_path, 'w', encoding='utf-8') as f:
        f.write("The weather is 20C today.\n")
        f.write("It will drop to -5C tonight.\n")
        f.write("The oven is set to 180C.\n")
        f.write("Room temperature is 25C.\n")
    
    converter = TemperatureConverter()
    
    with open(args.file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    result = converter.process_text(original_content)
    print(result)

if __name__ == '__main__':
    main()