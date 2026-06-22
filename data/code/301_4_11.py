import csv

def convert_date_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [row[0].strftime('%Y-%m-%d') if isinstance(row[0], datetime.date) else row[0] for row in reader]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_date_format('sample_input.csv', 'sample_output.csv')