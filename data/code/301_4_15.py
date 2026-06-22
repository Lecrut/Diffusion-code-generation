import csv

def convert_date_format(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [row[0]] + [row[1].strftime('%Y-%m-%d') if row[1] else None for row in zip(row, ['%m/%d/%Y'])]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')