import argparse
import re
import sys
import tempfile
import os

def convert_temperatures_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except PermissionError:
        return f"Error: Permission denied for file '{file_path}'."
    except Exception as e:
        return f"Error reading file: {e}"

    pattern = r'(-?\d+(?:\.\d+)?)\s*°C'
    
    def replace_match(match):
        celsius = float(match.group(1))
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.2f}°F"

    converted_content = re.sub(pattern, replace_match, content)
    
    if converted_content == content:
        return "No temperature values found in the file."
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    return converted_content

def main():
    parser = argparse.ArgumentParser(description="Convert Celsius temperatures to Fahrenheit in a file.")
    parser.add_argument("file_path", help="Path to the input file")
    args = parser.parse_args()

    result = convert_temperatures_in_file(args.file_path)
    print(result)

if __name__ == '__main__':
    temp_content = "Today the weather is 25°C. Tomorrow it might reach 30°C.\nEvening is 15°C."
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write(temp_content)
        tmp_file_path = tmp.name

    output = convert_temperatures_in_file(tmp_file_path)
    print(output)
    os.remove(tmp_file_path)