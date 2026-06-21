import csv

def parse_csv_first_column(csv_string):
    reader = csv.reader([csv_string], quotechar='"', escapechar='\\')
    first_column_values = [row[0] for row in reader]
    return first_column_values
if __name__ == '__main__':
    sample_csv = 'apple,"banana\\\\"peach",orange'
    result = parse_csv_first_column(sample_csv)
    print(result)