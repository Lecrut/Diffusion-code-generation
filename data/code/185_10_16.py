def parse_csv(csv_string):
    records = []
    for line in csv_string.split('\n'):
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue
        record = {
            'id': parts[0],
            'name': parts[1],
            'salary': float(parts[2])
        }
        records.append(record)
    return records

if __name__ == '__main__':
    csv_data = """1,John Doe,5000.0
2,Jane Smith,6000.5
3,Bob Johnson,7000.75"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)