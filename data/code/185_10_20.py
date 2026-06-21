import csv
from io import StringIO

def parse_csv(csv_string):
    records = []
    for row in csv.DictReader(StringIO(csv_string)):
        try:
            record = {
                'id': int(row['id']),
                'name': row['name'],
                'salary': float(row['salary'])
            }
            records.append(record)
        except ValueError as e:
            print(f"Error parsing record: {e}")
    return records

if __name__ == '__main__':
    csv_data = """id,name,salary
1,Alice,5000.75
2,Bob,6000.50
3,Charlie,7000.25"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)