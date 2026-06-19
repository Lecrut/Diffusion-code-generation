import argparse

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def process_file(input_path, output_path):
    try:
        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            for line in infile:
                try:
                    celsius = float(line.strip())
                    fahrenheit = convert_celsius_to_fahrenheit(celsius)
                    outfile.write(f'{fahrenheit}\n')
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File not found - {input_path}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument('input_file', type=str, help='Path to the input file containing Celsius temperatures')
    parser.add_argument('output_file', type=str, help='Path to the output file for Fahrenheit temperatures')
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)