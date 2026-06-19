import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        lines = content.splitlines()
        converted_lines = [f'{celsius_to_fahrenheit(float(line))}\n' for line in lines]
        with open(file_path, 'w') as file:
            file.writelines(converted_lines)
        return 'Conversion complete.'
    except Exception as e:
        return f'Error: {str(e)}'
if __name__ == '__main__':
    sample_file_content = '0\n25\n-40\n100'
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
    temp_file.write(sample_file_content)
    temp_file.close()
    result = convert_temperatures_in_file(temp_file.name)
    print(result)
    with open(temp_file.name, 'r') as file:
        print(file.read())