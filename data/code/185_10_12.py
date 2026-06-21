def parse_csv(csv_string):
    records = []
    for line in csv_string.split('\n'):
        if not line.strip():
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue
        try:
            record = {
                'id': int(parts[0]),
                'name': parts[1],
                'salary': float(parts[2])
            }
            records.append(record)
        except ValueError:
            continue
    return records

if __name__ == '__main__':
    csv_data = """1,Alice,50000.75
2,Bob,60000.50
3,Charlie,75000.25"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)