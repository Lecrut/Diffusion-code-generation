import argparse
import re
import os

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

def process_temperature_file(file_path):
    if not os.path.exists(file_path):
        return ""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    def replace_temperature(match):
        value_str = match.group(1)
        try:
            celsius = float(value_str)
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            return f"{fahrenheit:.2f}°F"
        except ValueError:
            return match.group(0)
    
    pattern = r'(-?\d+\.?\d*)°C'
    converted_content = re.sub(pattern, replace_temperature, content)
    return converted_content

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures from Celsius to Fahrenheit in a file.")
    parser.add_argument("--file", type=str, default="sample_temps.txt", help="Path to the file with temperature values")
    args = parser.parse_args()
    
    with open(args.file, 'w') as f:
        f.write("Temperature readings:\n")
        f.write("Room 1: 25.5°C\n")
        f.write("Room 2: -3.0°C\n")
        f.write("Room 3: 100°C\n")
        f.write("Outside: -40°C\n")
        f.write("Lab: 22.3°C\n")
    
    result = process_temperature_file(args.file)
    print(result)

if __name__ == '__main__':
    main()