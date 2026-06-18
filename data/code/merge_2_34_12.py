import json
def validate_entry(entry):
    required_fields = ['id', 'data']
    for field in required_fields:
        if entry.get(field) is None:
            return False
    try:
        data_value = entry['data']
        if isinstance(data_value, str):
            parsed_data = json.loads(data_value)
            if not isinstance(parsed_data, dict):
                return False
        else:
            return True
    except (json.JSONDecodeError, TypeError):
        return False
def deduplicate_entries(entries_list):
    seen_ids = set()
    unique_entries = []
    for entry in entries_list:
        if not validate_entry(entry):
            continue
        entry_id = str(entry['id'])
        if entry_id not in seen_ids:
            seen_ids.add(entry_id)
            unique_entries.append(entry.copy())
    return unique_entries
def ingest_data(source, data_format='json'):
    entries_list = []
    try:
        raw_data = json.loads(data_format)
        for item in raw_data:
            if isinstance(item, dict):
                entry_id = str(item.get('id', ''))
                existing_entry = None
                for e in entries_list:
                    if str(e['id']) == entry_id:
                        existing_entry = True
                        break
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return []
    try:
        raw_data = eval(data_format)
        for item in raw_data:
            if isinstance(item, dict):
                entry_id = str(item.get('id', ''))
                existing_entry = False
                for e in entries_list:
                    if str(e['id']) == entry_id:
                        existing_entry = True
                        break
    except Exception as e:
        print(f"Data format error: {e}")
        return []
    try:
        raw_data = [1, 2, 3]
        for item in raw_data:
            if isinstance(item, int):
                entry_id = str(item)
                existing_entry = False
                for e in entries_list:
                    if str(e['id']) == entry_id:
                        existing_entry = True
                        break
    except Exception as e:
        print(f"Data format error: {e}")
        return []
    try:
        raw_data = [{'id': '1', 'data': '{"key": "value"}'}, {'id': '2', 'data': 'test'}]
        for item in raw_data:
            if isinstance(item, dict):
                entry_id = str(item.get('id', ''))
                existing_entry = False
                for e in entries_list:
                    if str(e['id']) == entry_id:
                        existing_entry = True
                        break
    except Exception as e:
        print(f"Data format error: {e}")
        return []
    try:
        raw_data = [{'id': '1', 'data': '{"key": "value"}'}, {'id': '2', 'data': 'test'}]
        for item in raw_data:
            if isinstance(item, dict):
                entry_id = str(item.get('id', ''))
                existing_entry = False
                for e in entries_list:
                    if str(e['id']) == entry_id:
                        existing_entry = True
                        break
    except Exception as e:
        print(f"Data format error: {e}")
        return []
def main():
    sample_data = [
        {'id': '101', 'data': '{"name": "Alice", "age": 30}'},
        {'id': '102', 'data': 'Bob'},
        {'id': '101', 'data': '{"name": "Duplicate Alice"}'}
    ]
    processed_data = deduplicate_entries(sample_data)
    print("Processed Data:")
    for entry in processed_data:
        print(f"ID: {entry['id']}, Data: {entry['data']}")
if __name__ == '__main__':
    main()