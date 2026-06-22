import argparse
import re
import sys
import io

def convert_temperatures_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Unable to read file."

    pattern = r'(-?\d+(?:\.\d+)?)\s*C'
    
    def replace_match(match):
        celsius = float(match.group(1))
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.2f} F"

    converted_content = re.sub(pattern, replace_match, content)
    return converted_content

def create_temp_file():
    filename = "temp_sample.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("The current temperature is 25 C outside.\n")
        f.write("Yesterday it was 30.5 C in the afternoon.\n")
        f.write("At night it dropped to -5 C.\n")
        f.write("Some text without temperature like 100 C is not a real temp but 100C matches.\n")
        f.write("No temperature here: 12345\n")
    return filename

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Celsius temperatures to Fahrenheit in a file.")
    parser.add_argument("file_path", nargs="?", default=None, help="Path to the input file")
    
    if parser.parse_args().file_path is None:
        temp_filename = create_temp_file()
        args = parser.parse_args([temp_filename])
    else:
        args = parser.parse_args()
    
    result = convert_temperatures_in_file(args.file_path)
    print(result)