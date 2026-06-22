import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def batch_convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                output_file.write(f'{fahrenheit}\n')
    except FileNotFoundError:
        print('Error: The input file does not exist.')
    except ValueError:
        print('Error: The input file contains non-numeric data.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    sample_input_data = '10\n20\n30\n40\n50'
    sample_output_path = 'output.txt'
    with open('sample_input.txt', 'w') as temp_file:
        temp_file.write(sample_input_data)
    batch_convert_temperatures('sample_input.txt', sample_output_path)
    with open(sample_output_path, 'r') as result_file:
        print(result_file.read())