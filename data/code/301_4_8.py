import csv

def convert_date_format(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [row[0].split('/')[2] + '-' + row[0].split('/')[0] + '-' + row[0].split('/')[1]] + row[1:]
            writer.writerow(new_row)

if __name__ == '__main__':
    convert_date_format('input.csv', 'output.csv')