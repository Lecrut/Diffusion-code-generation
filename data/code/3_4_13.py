import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Convert Celsius temperatures to Fahrenheit in a text file.")
    parser.add_argument("file_path", type=str, help="Path to the input file containing temperature values.")
    return parser.parse_args()

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def convert_file_to_fahrenheit(file_path):
    if not os.path.exists(file_path):
        return ""
    
    with open(file_path, "r") as f:
        content = f.read()
    
    import re
    
    pattern = r'(\d+\.?\d*)\s*°\s*[Cc]els[iu]s'
    
    def replace_celsius(match):
        temp_c = float(match.group(1))
        temp_f = celsius_to_fahrenheit(temp_c)
        return f"{temp_f:.2f} °Fahrenheit"
    
    converted_content = re.sub(pattern, replace_celsius, content)
    
    return converted_content

if __name__ == '__main__':
    temp_data = "The weather today is 20 °Celsius and tomorrow is 25 Celsius."
    
    temp_file = "temp_input.txt"
    
    with open(temp_file, "w") as f:
        f.write(temp_data)
    
    result = convert_file_to_fahrenheit(temp_file)
    
    os.remove(temp_file)
    
    print(result)