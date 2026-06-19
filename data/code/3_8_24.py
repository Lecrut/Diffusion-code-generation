import csv

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                if len(row) > 0 and row[0].isdigit():
                    fahrenheit = celsius_to_fahrenheit(float(row[0]))
                    writer.writerow([fahrenheit])
    except FileNotFoundError:
        print(f'Error: The file {input_file} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sample_output.csv'
    with open(input_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['0'])
        writer.writerow(['100'])
    convert_temperatures(input_csv, output_csv)
    with open(output_csv, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])