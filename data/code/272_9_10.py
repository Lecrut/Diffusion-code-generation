import csv

def sort_csv_rows_by_first_column(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    sorted_rows = sorted(rows, key=lambda row: row[0])

    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(sorted_rows)

if __name__ == '__main__':
    input_csv_path = 'sample_input.csv'
    output_csv_path = 'sorted_output.csv'
    sort_csv_rows_by_first_column(input_csv_path, output_csv_path)