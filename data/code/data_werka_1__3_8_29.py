import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, mode='r', newline='') as input_file:
            reader = csv.reader(input_file)
            header = next(reader)
            data = [row for row in reader]
        converted_data = []
        for row in data:
            celsius_temp = float(row[0])
            fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
            converted_data.append([fahrenheit_temp] + row[1:])
        with open(output_file_path, mode='w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerows(converted_data)
    except FileNotFoundError:
        print(f'Error: The file {input_file_path} does not exist.')
    except IOError:
        print('An error occurred while reading or writing the file.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    sample_data = [['25', 'LocationA'], ['30', 'LocationB'], ['18', 'LocationC']]
    with open(input_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Temperature', 'Location'])
        writer.writerows(sample_data)
    convert_temperatures(input_csv, output_csv)
    with open(output_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)