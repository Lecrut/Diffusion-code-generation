import csv

def parse_csv_column(csv_string):
    reader = csv.reader([csv_string], quotechar='"', escapechar='\\')
    first_column = [row[0] for row in reader]
    return first_column

if __name__ == '__main__':
    sample_csv = 'apple,"banana\"s",cherry'
    print(parse_csv_column(sample_csv))