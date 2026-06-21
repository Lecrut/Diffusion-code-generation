def parse_csv(csv_string):
    records = []
    for line in csv_string.strip().split('\n'):
        parts = line.split(',')
        if len(parts) == 3:
            record = {
                'id': int(parts[0]),
                'name': parts[1],
                'salary': float(parts[2])
            }
            records.append(record)
    return records

if __name__ == '__main__':
    csv_data = """1,Alice,5000.75
2,Bob,6000.50
3,Charlie,7000.25"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)