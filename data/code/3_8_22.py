import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, mode='r', newline='') as input_file:
            reader = csv.reader(input_file)
            header = next(reader)
            data = [row for row in reader]
        converted_data = [[celsius_to_fahrenheit(float(row[0])), *row[1:]] for row in data]
        with open(output_file_path, mode='w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Fahrenheit'] + header[1:])
            writer.writerows(converted_data)
    except FileNotFoundError:
        print(f'Error: The file {input_file_path} was not found.')
    except ValueError:
        print('Error: Invalid temperature value in the input file.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    sample_data = [['25', 'CityA'], ['30', 'CityB'], ['15', 'CityC']]
    with open(input_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Celsius', 'Location'])
        writer.writerows(sample_data)
    convert_temperatures(input_csv, output_csv)