import re
import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except IOError as e:
        return f"Error reading file: {e}"

    pattern = r'(-?\d+(?:\.\d+)?)\s*C\b'
    
    def replace_match(match):
        celsius_value = float(match.group(1))
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        return f"{fahrenheit_value:.2f}F"
    
    converted_content = re.sub(pattern, replace_match, content)
    return converted_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert temperatures from Celsius to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the file containing temperature values.')
    args = parser.parse_args()
    
    sample_file_path = "sample_temperatures.txt"
    sample_content = "Today is 20C and tomorrow it will be -5C. The boiling point is 100C."
    
    with open(sample_file_path, 'w') as f:
        f.write(sample_content)
    
    result = convert_temperatures_in_file(args.file_path if args.file_path else sample_file_path)
    print(result)