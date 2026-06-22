import csv

DATE_FORMAT_INPUT = '%m/%d/%Y'
DATE_FORMAT_OUTPUT = '%Y-%m-%d'

def convert_date_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            new_row = [row[0].strftime(DATE_FORMAT_OUTPUT) if row[0] else None]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')