import csv
from datetime import datetime

def convert_date_format(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                new_row = [datetime.strptime(row[0], '%m/%d/%Y').strftime('%Y-%m-%d') if row[0] else None]
                writer.writerow(new_row)
    except FileNotFoundError:
        print("Input file not found.")
    except ValueError:
        print("Invalid date format in input file.")

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')