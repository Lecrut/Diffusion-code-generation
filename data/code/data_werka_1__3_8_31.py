import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                if len(row) > 0 and row[0].strip().lower() == 'celsius':
                    writer.writerow(['Fahrenheit'])
                else:
                    try:
                        celsius_value = float(row[0])
                        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
                        writer.writerow([fahrenheit_value])
                    except ValueError:
                        print(f'Skipping invalid temperature value: {row[0]}')
    except FileNotFoundError:
        print(f'Error: The file {input_file} was not found.')
    except IOError as e:
        print(f'An I/O error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'temperatures_celsius.csv'
    output_csv = 'temperatures_fahrenheit.csv'
    sample_data = 'celsius\n    0\n    100\n    -40\n    invalid'
    with open(input_csv, 'w', newline='') as f:
        f.write(sample_data)
    convert_temperatures(input_csv, output_csv)