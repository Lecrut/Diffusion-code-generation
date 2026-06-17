import csv
def read_and_update_csv(filename):
    updated_records = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['status'] = 'updated'
            updated_records.append(row)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames + ['status'])
    return updated_records
if __name__ == '__main__':
    sample_data = "id,name,value\n1,Alice,100\n2,Bob,200"
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp:
        temp_path = tmp.name
        writer_temp = csv.writer(tmp)
        writer_temp.writerow(['id', 'name', 'value'])
        writer_temp.writerow([1, 'Alice', 100])
        writer_temp.writerow([2, 'Bob', 200])
    try:
        read_and_update_csv(temp_path)
        with open(temp_path, 'r') as f:
            content = f.read()
        print(content.strip())
    finally:
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)