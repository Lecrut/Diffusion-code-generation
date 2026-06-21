import csv
from io import StringIO
SALARY_FIELD = 'salary'

def parse_csv(csv_string):
    records = []
    for row in csv.DictReader(StringIO(csv_string)):
        record = {key: float(value) if key == SALARY_FIELD else value for key, value in row.items()}
        records.append(record)
    return records
if __name__ == '__main__':
    sample_csv = 'id,name,salary\n1,Alice,50000.75\n2,Bob,60000.50'
    parsed_records = parse_csv(sample_csv)
    print(parsed_records)