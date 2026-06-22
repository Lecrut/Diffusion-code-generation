import argparse

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        converted_lines = []
        for line in lines:
            try:
                celsius_value = float(line.strip())
                fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
                converted_lines.append(f'{fahrenheit_value}\n')
            except ValueError:
                converted_lines.append(line)
        return ''.join(converted_lines)
    except FileNotFoundError:
        return 'File not found.'
if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    sample_content = '-10\n0\n25\n37.5\nabc\n100'
    with open(sample_file_path, 'w') as file:
        file.write(sample_content)
    result = process_file(sample_file_path)
    print(result)