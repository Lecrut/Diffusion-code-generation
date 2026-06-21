import csv

def parse_csv_first_column(csv_string):
    reader = csv.reader([csv_string], quotechar='"', escapechar='\\')
    return [row[0] for row in reader if len(row) > 0]

if __name__ == '__main__':
    sample_csv = 'apple,"banana \"with quotes\"",cherry\n"dog \\cat",elephant,frog'
    print(parse_csv_first_column(sample_csv))