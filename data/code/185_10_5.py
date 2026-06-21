import csv

def parse_csv(csv_string):
    records = []
    reader = csv.DictReader(csv_string.splitlines())
    for row in reader:
        row['salary'] = float(row['salary'])
        records.append(row)
    return records

if __name__ == '__main__':
    sample_csv = """id,name,salary
1,Alice,50000.75
2,Bob,60000.50"""
    parsed_records = parse_csv(sample_csv)
    print(parsed_records)