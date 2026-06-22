import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    converted_lines = []
    for line in lines:
        try:
            celsius_value = float(line.strip())
            fahrenheit_value = celsius_to_fahrenheit(celsius_value)
            converted_lines.append(f"{fahrenheit_value}\n")
        except ValueError:
            converted_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(converted_lines)

if __name__ == '__main__':
    sample_file_path = "sample_temperatures.txt"
    sample_content = "-40\n0\n100\n37.5\nabc\n25"
    
    with open(sample_file_path, 'w') as file:
        file.write(sample_content)
    
    convert_temperatures_in_file(sample_file_path)
    
    with open(sample_file_path, 'r') as file:
        converted_content = file.read()
        print(converted_content)