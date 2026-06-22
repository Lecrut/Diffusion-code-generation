import csv
from datetime import datetime

def convert_date_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            try:
                date_obj = datetime.strptime(row[0], '%m/%d/%Y')
                new_row = [date_obj.strftime('%Y-%m-%d')]
                writer.writerow(new_row)
            except ValueError:
                print(f"Invalid date format: {row[0]}")
                continue

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')