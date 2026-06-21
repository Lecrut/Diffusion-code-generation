import csv
from io import StringIO

def parse_csv_first_column(csv_string):
    first_column = []
    with StringIO(csv_string) as csvfile:
        reader = csv.reader(csvfile, quotechar='"', escapechar='\\')
        for row in reader:
            if row:
                first_column.append(row[0])
    return first_column

if __name__ == '__main__':
    sample_csv = 'apple,"banana\"s",cherry\n"dog\\cat",elephant,frog'
    print(parse_csv_first_column(sample_csv))