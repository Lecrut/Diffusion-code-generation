import argparse
import re
import tempfile
import os

def convert_temps_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    def replace_celsius(match):
        celsius = float(match.group(1))
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit}F"
    
    pattern = r'(\d+(?:\.\d+)?)C'
    converted_content = re.sub(pattern, replace_celsius, content)
    
    with open(file_path, 'w') as f:
        f.write(converted_content)
    
    return converted_content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    
    sample_content = "The water boils at 100C and freezes at 0C.\nRoom temperature is 22.5C.\n"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write(sample_content)
        temp_file_path = temp_file.name
    
    try:
        result = convert_temps_in_file(temp_file_path)
        print(result)
    finally:
        os.unlink(temp_file_path)