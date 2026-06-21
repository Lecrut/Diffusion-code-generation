def parse_csv(csv_string):
    records = []
    lines = csv_string.split('\n')
    header = lines[0].split(',')
    
    for line in lines[1:]:
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
    sample_csv = """id,name,salary
4,David,7000.25
5,Eve,8000.75"""
    parsed_records = parse_csv(sample_csv)
    print(parsed_records)