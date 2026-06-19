import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file_path, output_file_path):
    try:
        with open(input_file_path, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            data = [row for row in reader]
        converted_data = []
        for row in data:
            celsius_temp = float(row[0])
            fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
            converted_data.append([fahrenheit_temp])
        with open(output_file_path, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Temperature (F)'])
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
    sample_data = [['0'], ['100'], ['-40']]
    with open(input_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Temperature (C)'])
        writer.writerows(sample_data)
    convert_temperatures(input_csv, output_csv)