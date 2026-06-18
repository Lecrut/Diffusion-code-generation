import csv
def read_csv_to_dict(file_path):
    data = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = tuple(row.keys()) + (row['id'],) if 'id' in row else None
            data[key] = dict(row)
    return data
def update_csv_records(input_file, output_file):
    records_to_update = [
        {'id': 101, 'name': 'Alice', 'age': 35},
        {'id': 204, 'city': 'New York'},
        {'id': 998, 'status': 'active'}
    ]
    with open(input_file, mode='r', newline='', encoding='utf-8') as input_f:
        reader = csv.DictReader(input_f)
        fieldnames = reader.fieldnames or []
        temp_data = {}
        for row in reader:
            key = tuple(fieldnames[:fieldnames.index('id')+1]) + (row['id'],) if 'id' in fieldnames else None
            if not key: continue
            temp_data[key] = dict(row)
    updated_records_count = 0
    for record in records_to_update:
        id_val = str(record['id'])
        found_key = None
        for k, v in temp_data.items():
            if isinstance(k[1], int):
                current_id = k[1]
            else:
                continue
            is_match = True
            update_fields = record.keys() - {'id'}
            for field in update_fields:
                if v.get(field) != str(record[field]):
                    is_match = False
                    break
            if is_match and current_id == id_val:
                found_key = k
        if not found_key:
             for k in temp_data.keys():
                 if str(k[1]) == id_val:
                     found_key = k
                     break
        if found_key:
            new_row_dict = dict(temp_data.get(found_key, {}))
            for key, value in record.items():
                field_name = None
                try:
                    idx = temp_data[found_key].index(key)
                    field_name = found_key[idx] if isinstance(idx, int) else None
                    new_row_dict[field_name] = str(value)
                except (ValueError, TypeError):
                     pass
            temp_data[found_key] = new_row_dict
            updated_records_count += 1
    with open(output_file, mode='w', newline='', encoding='utf-8') as output_f:
        writer = csv.DictWriter(output_f, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(temp_data.keys()):
            row_dict = dict(temp_data[key])
            final_row = {}
            for i, fname in enumerate(fieldnames):
                val = str(row_dict.get(fname))
                try:
                    idx = key.index(i) + 1 
                    if isinstance(idx, int):
                        pass                                     
                except ValueError:
                     continue
                final_row[fname] = val
            writer.writerow(final_row)
    return updated_records_count
if __name__ == '__main__':
    input_file = 'sample_data.csv'
    output_file = 'updated_sample_data.csv'
    count = update_csv_records(input_file, output_file)
    print(f"Updated {count} records.")