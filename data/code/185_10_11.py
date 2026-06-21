def parse_csv(csv_string):
    records = []
    lines = csv_string.strip().split('\n')
    for line in lines:
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
    csv_data = """1,Alice,5000.75
2,Bob,6000.50
3,Charlie,7000.25"""
    parsed_records = parse_csv(csv_data)
    print(parsed_records)