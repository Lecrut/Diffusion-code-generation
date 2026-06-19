import argparse

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def batch_convert(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            for line in infile:
                try:
                    celsius = float(line.strip())
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    outfile.write(f'{fahrenheit}\n')
                except ValueError:
                    print(f'Error: Non-numeric value encountered and skipped - {line.strip()}')
    except FileNotFoundError:
        print('Error: Input file not found.')
    except IOError as e:
        print(f'IO Error: {e}')
if __name__ == '__main__':
    input_file_path = 'sample_input.txt'
    output_file_path = 'sample_output.txt'
    sample_data = '0\n25\n-40\n100\nabc\n37'
    with open(input_file_path, 'w') as f:
        f.write(sample_data)
    batch_convert(input_file_path, output_file_path)