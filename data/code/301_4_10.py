import csv
from datetime import datetime

def convert_date_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            date_str = row[0]
            if date_str:
                try:
                    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                    new_date_str = date_obj.strftime('%Y-%m-%d')
                    writer.writerow([new_date_str])
                except ValueError:
                    writer.writerow([None])
            else:
                writer.writerow([None])

if __name__ == '__main__':
    sample_input_file = 'sample_input.csv'
    sample_output_file = 'sample_output.csv'
    
    with open(sample_input_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['01/01/2024'])
        writer.writerow(['12/31/2023'])
        writer.writerow(['invalid date'])
    
    convert_date_format(sample_input_file, sample_output_file)
    
    with open(sample_output_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])