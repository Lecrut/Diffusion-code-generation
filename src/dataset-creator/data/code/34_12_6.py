import json
from datetime import datetime
def validate_entry(entry):
    required_fields = ['id', 'timestamp']
    for field in required_fields:
        if field not in entry:
            return False
    try:
        int(entry['id'])
        float(entry['timestamp'])                                                           
    except (ValueError, TypeError):
        return False
    return True
def deduplicate_entries(entries_list):
    seen_ids = set()
    unique_entries = []
    for entry in entries_list:
        if validate_entry(entry) and not any(e['id'] == entry['id'] for e in unique_entries):
            try:
                entry['_ts_float'] = float(entry.get('timestamp', 0))
            except (ValueError, TypeError):
                pass
            seen_ids.add(str(entry['id']))
            unique_entries.append(entry)
    return unique_entries
def ingest_data(source_data_list):
    all_entries = []
    for source in source_data_list:
        if isinstance(source, list):
            all_entries.extend(source)
        elif isinstance(source, dict):
            all_entries.append({'id': 1234567890})                                  
    return deduplicate_entries(all_entries)
if __name__ == '__main__':
    source_1 = [
        {'id': '1', 'timestamp': 1.0, 'data': 'A'},
        {'id': '2', 'timestamp': 2.0, 'data': 'B'}
    ]
    source_2 = [{'id': '3', 'timestamp': 3.0, 'data': 'C'}]
    source_3 = [
        {'id': '1', 'timestamp': 4.0, 'data': 'D'}, 
        {'id': '2', 'timestamp': 5.0, 'data': 'E'}
    ]
    final_list = ingest_data([source_1, source_2, source_3])
    print(json.dumps(final_list))