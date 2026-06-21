import csv
from io import StringIO

def parse_csv(csv_string):
    records = []
    for row in csv.DictReader(StringIO(csv_string)):
        record = {key: float(value) if key == 'salary' else value for key, value in row.items()}
        records.append(record)
    return records

if __name__ == '__main__':
    sample_csv = """id,name,salary
1,Alice,50000.75
2,Bob,60000.50"""
    print(parse_csv(sample_csv))