import argparse
import sys
import os
import re

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def convert_file_content(content):
    pattern = re.compile(r'(-?\d+(?:\.\d+)?)\s*C\s*$|C\s*=\s*(-?\d+(?:\.\d+))')
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        match_start = pattern.search(line)
        if match_start:
            full_match = match_start.group(0)
            if match_start.group(1) is not None:
                temp_val = match_start.group(1)
                new_temp = celsius_to_fahrenheit(float(temp_val))
                replacement = f"{new_temp:.2f}"
                new_line = line.replace(full_match, replacement)
            else:
                temp_val = match_start.group(2)
                new_temp = celsius_to_fahrenheit(float(temp_val))
                replacement = f"{new_temp:.2f}"
                new_line = line.replace(full_match, replacement)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def process_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, 'r') as f:
        content = f.read()
    converted_content = convert_file_content(content)
    return converted_content

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures from Celsius to Fahrenheit in a file.")
    parser.add_argument('file_path', type=str, help="Path to the input file.")
    args = parser.parse_args(['test_data.txt'])
    temp_c = 100
    temp_f = celsius_to_fahrenheit(temp_c)
    print(temp_f)

if __name__ == '__main__':
    main()