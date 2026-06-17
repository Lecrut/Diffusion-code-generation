import csv
def read_csv(file_path):
    records = []
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row.copy())
    return records
def update_records(records, target_id, new_data):
    updated_count = 0
    for record in records:
        if str(record.get('id', '')) == str(target_id):
            for key, value in new_data.items():
                record[key] = value
            updated_count += 1
            break
    return records
def write_csv(file_path, records):
    fieldnames = list(records[0].keys()) if records else []
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)
def main():
    file_name = "data.csv"
    if not __import__('os').path.exists(file_name):
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'email'])
            for row in [['101', 'Alice', 'alice@example.com'], ['102', 'Bob', 'bob@example.com']]:
                writer.writerow(row)
    records = read_csv(file_name)
    updated_records = update_records(records, 101, {'name': 'Alice Smith', 'email': 'new_alice@example.com'})
    write_csv(file_name, updated_records)
if __name__ == '__main__':
    main()