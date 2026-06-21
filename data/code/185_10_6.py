def parse_csv(csv_string):
    records = []
    for line in csv_string.strip().split('\n'):
        fields = line.split(',')
        if len(fields) == 3:
            record = {
                'id': int(fields[0]),
                'name': fields[1],
                'salary': float(fields[2])
            }
            records.append(record)
    return records

if __name__ == '__main__':
    csv_data = """1,John Doe,5000.75
2,Jane Smith,6000.50
3,Bob Johnson,5500.00"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)