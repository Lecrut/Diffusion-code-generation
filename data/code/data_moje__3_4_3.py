import argparse
import re
import os

def convert_temperatures_in_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    def replace_celsius(match):
        value = float(match.group(1))
        fahrenheit = (value * 9/5) + 32
        return f"{fahrenheit:.2f} F"
    
    pattern = r'(-?\d+(?:\.\d+)?)\s*C'
    converted_content = re.sub(pattern, replace_celsius, content)
    return converted_content

if __name__ == '__main__':
    sample_file_path = "temp_data.txt"
    with open(sample_file_path, 'w') as f:
        f.write("Today is 20 C and tomorrow will be 25 C.\n")
        f.write("The freezer is set to -18 C.\n")
        f.write("Room temperature is around 22.5 C.\n")
    
    result = convert_temperatures_in_file(sample_file_path)
    print(result)