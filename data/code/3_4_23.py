import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    converted_lines = []
    for line in lines:
        try:
            celsius_value = float(line.strip())
            fahrenheit_value = celsius_to_fahrenheit(celsius_value)
            converted_lines.append(f'{fahrenheit_value}\n')
        except ValueError:
            converted_lines.append(line)
    with open(file_path, 'w') as file:
        file.writelines(converted_lines)
if __name__ == '__main__':
    sample_file_content = '0\n25\n100\n-40\nnot_a_number\n37'
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(sample_file_content)
        temp_file_path = temp_file.name
    convert_temperatures_in_file(temp_file_path)
    with open(temp_file_path, 'r') as file:
        print(file.read())