import argparse
import sys
import re

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, 'r') as f:
        content = f.read()

    def replace_temp(match):
        sign = match.group(1) or ''
        value = match.group(2)
        try:
            temp_c = float(value)
            temp_f = celsius_to_fahrenheit(temp_c)
            if temp_f == int(temp_f):
                result_str = f'{int(temp_f)}'
            else:
                result_str = f'{temp_f:.2f}'
            return f'{sign}{result_str}°F'
        except ValueError:
            return match.group(0)
    pattern = re.compile('([+-]?)\\.?\\d+(?:\\.\\d+)?(?=\\s*\\u00b0C|\\s*C\\s*$)')
    new_content = pattern.sub(replace_temp, content)
    with open(output_file_path, 'w') as f:
        f.write(new_content)
if __name__ == '__main__':
    sample_input_content = 'Room temp is 20°C. Freezing is 0°C. Boiling is 100°C.'
    sample_output_content = 'Room temp is 68.00°F. Freezing is 32°F. Boiling is 212°F.'
    temp_parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit in a file.')
    temp_parser.add_argument('--input', type=str, default='temp_input.txt', help='Input file path')
    temp_parser.add_argument('--output', type=str, default='temp_output.txt', help='Output file path')
    args = temp_parser.parse_args([])
    with open(args.input, 'w') as f:
        f.write(sample_input_content)
    convert_temperatures(args.input, args.output)
    with open(args.output, 'r') as f:
        result = f.read()
    print(result)