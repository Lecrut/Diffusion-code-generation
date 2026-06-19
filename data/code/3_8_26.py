import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, mode='r', newline='') as infile, open(output_file_path, mode='w', newline='') as outfile:
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
        print(f'Error: The file {input_file_path} was not found.')
    except IOError as e:
        print(f'An I/O error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    sample_data = [['Celsius'], [0], [100], [-40], ['invalid']]
    with open(input_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    convert_temperatures(input_csv, output_csv)
    with open(output_csv, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])