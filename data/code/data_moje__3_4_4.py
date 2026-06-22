import re
import argparse

def convert_celsius_to_fahrenheit(match):
    celsius_value = float(match.group(1))
    fahrenheit_value = celsius_value * 9 / 5 + 32
    return f"{fahrenheit_value:.2f}"

def convert_file_temperatures(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    pattern = r'(\d+(?:\.\d+)?)°?C'
    converted_content = re.sub(pattern, lambda m: f"{float(m.group(1)) * 9 / 5 + 32:.2f}°F", content)
    with open(file_path, 'w') as file:
        file.write(converted_content)
    return converted_content

def main():
    parser = argparse.ArgumentParser(description="Convert temperatures from Celsius to Fahrenheit in a file.")
    parser.add_argument("file_path", help="Path to the file containing temperature values in Celsius")
    args = parser.parse_args()
    result = convert_file_temperatures(args.file_path)
    print(result)

if __name__ == '__main__':
    sample_file_path = "sample_temperatures.txt"
    with open(sample_file_path, 'w') as f:
        f.write("The temperature is 25°C today.\nIt was 30°C yesterday.\nNow it's 20°C.")
    result = convert_file_temperatures(sample_file_path)
    print(result)