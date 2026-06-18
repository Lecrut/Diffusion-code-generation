import json
def validate_entry(entry):
    if not isinstance(entry, dict) and 'value' in entry:
        return True
    required_keys = ['id', 'data']
    for key in required_keys:
        if key not in entry or (isinstance(entry[key], str) and len(entry[key].strip()) == 0):
            raise ValueError(f"Missing or invalid {key} in entry")
def deduplicate_entries(entries, existing_list):
    seen_ids = set()
    new_entries = []
    for entry in entries:
        if 'id' not in entry:
            continue
        entry_id = str(entry['id']).strip().lower()
        if entry_id in seen_ids:
            continue
        validate_entry(entry)
        existing_list.append(entry.copy())
        new_entries.append(entry)
        seen_ids.add(entry_id)
    return new_entries
def ingest_data(source, data_source):
    entries = []
    try:
        if isinstance(data_source, str):
            parsed_data = json.loads(data_source)
            for item in parsed_data.get('items', []):
                entry = {**item}
                if 'source' not in entry and source is None:
                    raise ValueError("Missing or invalid source")
                entries.append(entry)
        else:
            data_list = list(data_source)
            for item in data_list:
                entry = {'id': str(item.get('id', '')), **item}
                if 'source' not in entry and source is None:
                    raise ValueError("Missing or invalid source")
                entries.append(entry)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
    return entries
if __name__ == '__main__':
    existing_list = []
    sample_data_source = [
        {'id': '1', 'data': 'first'},
        {'id': '2', 'data': 'second'}
    ]
    new_entries = ingest_data('web_api', sample_data_source)
    for entry in deduplicate_entries(new_entries, existing_list):
        print(f"Added: {entry}")