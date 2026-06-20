import argparse
import re
import sys
import io

def convert_file_temps(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    def replace_celsius(match):
        value = float(match.group(1))
        fahrenheit = (value * 9/5) + 32
        return f"{fahrenheit:.2f}F"
    
    pattern = r'(-?\d+\.?\d*)\s*C\b'
    new_content = re.sub(pattern, replace_celsius, content)
    return new_content

if __name__ == '__main__':
    sample_data = "The temperature is 25 C today.\nIt dropped to -5 C last night.\nAnother reading: 100 C."
    temp_file = "sample_temp.txt"
    
    with open(temp_file, 'w') as f:
        f.write(sample_data)
    
    result = convert_file_temps(temp_file)
    print(result)