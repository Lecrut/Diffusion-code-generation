import csv
from io import StringIO

def extract_first_column(csv_data):
    result = []
    try:
        reader = csv.reader(StringIO(csv_data), quotechar='"')
        for row in reader:
            if row and row[0]:
                result.append(row[0])
    except Exception as e:
        raise ValueError("Invalid CSV data") from e
    return result

if __name__ == '__main__':
    sample_csv = """\
"Hello", "World"
"Python", "is fun"
"abc", "123"
"""
    print(extract_first_column(sample_csv))