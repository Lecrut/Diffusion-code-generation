import argparse
import re
import sys
import os
import tempfile

def convert_temperatures(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"

    pattern = r'(\d+(?:\.\d+)?)\s*C'
    
    def replace_func(match):
        celsius = float(match.group(1))
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.2f} F"
    
    result = re.sub(pattern, replace_func, content, flags=re.IGNORECASE)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert temperature values from Celsius to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    
    temp_dir = tempfile.gettempdir()
    sample_file_path = os.path.join(temp_dir, 'temp_sample.txt')
    
    sample_content = """The temperature today is 25 C.
Yesterday it was 30.5 C.
Tomorrow forecast predicts 18 C.
No temperature mentioned here.
Double check: 0 C and 100 C.
"""
    
    with open(sample_file_path, 'w') as f:
        f.write(sample_content)
    
    result = convert_temperatures(sample_file_path)
    print(result)
    
    if os.path.exists(sample_file_path):
        os.remove(sample_file_path)