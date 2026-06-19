import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            data = [row for row in reader]
        converted_data = []
        for row in data:
            new_row = []
            for value in row:
                try:
                    celsius = float(value)
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    new_row.append(fahrenheit)
                except ValueError:
                    new_row.append(value)
            converted_data.append(new_row)
        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(converted_data)
    except FileNotFoundError:
        print(f'Error: The file {input_file} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    convert_temperatures(input_csv, output_csv)