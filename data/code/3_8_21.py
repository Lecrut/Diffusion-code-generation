import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                if len(row) > 0 and row[0].strip().isdigit():
                    celsius_temp = float(row[0])
                    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
                    writer.writerow([fahrenheit_temp])
    except FileNotFoundError:
        print(f'Error: The file {input_file} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    sample_data = [['0'], ['100'], ['-40']]
    with open(input_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    convert_temperatures(input_csv, output_csv)