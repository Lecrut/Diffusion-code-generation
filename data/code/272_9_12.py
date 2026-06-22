import csv

def sort_csv_by_first_column(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        data = sorted(reader, key=lambda row: row[0])
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

if __name__ == '__main__':
    sort_csv_by_first_column('input.csv', 'output.csv')