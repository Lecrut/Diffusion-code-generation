import csv
from io import StringIO

def parse_employee_records(csv_string):
    records = []
    for row in csv.DictReader(StringIO(csv_string)):
        row['salary'] = float(row['salary'])
        records.append(row)
    return records

if __name__ == '__main__':
    sample_csv = """id,name,salary
1,Alice,50000.00
2,Bob,60000.00
3,Charlie,70000.00"""
    employees = parse_employee_records(sample_csv)
    print(employees)