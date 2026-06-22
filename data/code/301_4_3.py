import csv

def convert_date_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [row[0].replace('/', '-') if row[0] else None]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')