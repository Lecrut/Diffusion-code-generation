import csv

def convert_dates(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            new_row = [row[0]] + [row[1].strftime('%Y-%m-%d') if isinstance(row[1], datetime.date) else row[1] for row[1] in row[2:]]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_dates('input.csv', 'output.csv')