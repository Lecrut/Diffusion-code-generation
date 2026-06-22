import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
        converted_lines = []
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                converted_lines.append(f'{fahrenheit}\n')
            except ValueError:
                print(f'Skipping invalid temperature value: {line.strip()}')
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(converted_lines)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    input_sample = 'sample_input.txt'
    output_sample = 'sample_output.txt'
    with open(input_sample, 'w') as f:
        f.write('0\n25\n-40\n100\ninvalid\n')
    convert_temperatures(input_sample, output_sample)