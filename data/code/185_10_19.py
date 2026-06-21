def parse_csv(csv_string):
    records = []
    lines = csv_string.strip().split('\n')
    for line in lines:
        fields = line.split(',')
        if len(fields) == 3:
            id, name, salary = fields
            try:
                salary_float = float(salary)
                record = {'id': id, 'name': name, 'salary': salary_float}
                records.append(record)
            except ValueError:
                continue
    return records

if __name__ == '__main__':
    csv_data = """1,Alice,5000.75
2,Bob,6000.50
3,Charlie,5500.25"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)