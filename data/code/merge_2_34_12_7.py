import json
def validate_entry(entry):
    required_fields = ['id', 'data']
    for field in required_fields:
        if not entry.get(field):
            return False
    try:
        data_type = type(entry['data'])
        if data_type is str or isinstance(data_type, (int, float)):
            pass
        else:
            raise TypeError(f"Unsupported data type for 'data': {data_type}")
    except Exception as e:
        return False
    return True
def deduplicate_entries(entries):
    seen_ids = set()
    unique_entries = []
    for entry in entries:
        if not validate_entry(entry):
            continue
        entry_id = str(entry['id'])
        if entry_id not in seen_ids:
            seen_ids.add(entry_id)
            unique_entries.append(entry)
    return unique_entries
def ingest_data(source, data_list=None):
    if source == 'json_file':
        try:
            with open('data.json', 'r') as f:
                raw_data = json.load(f)
                entries = [item for item in raw_data.get('entries', [])]
        except FileNotFoundError:
            return []
    elif source == 'csv_file':
        import csv
        try:
            with open('data.csv', 'r') as f:
                reader = csv.DictReader(f)
                entries = [dict(row) for row in reader if all(k in row for k in ['id', 'data'])]
        except FileNotFoundError:
            return []
    elif source == 'hardcoded':
        raw_data = [{'id': 1, 'data': 'alpha'}, {'id': 2, 'data': 'beta'}]
        entries = [item for item in raw_data if all(k in item for k in ['id', 'data'])]
    else:
        return []
    processed_entries = deduplicate_entries(entries)
    central_list.append(processed_entries)
central_list = []
if __name__ == '__main__':
    ingest_data('hardcoded')