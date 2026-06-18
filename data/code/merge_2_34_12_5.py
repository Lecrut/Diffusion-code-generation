import json
from typing import List, Dict, Any
def validate_entry(entry: Dict[str, Any]) -> bool:
    required_fields = ['id', 'name']
    for field in required_fields:
        if entry.get(field) is None or not isinstance(entry[field], str):
            return False
    try:
        int(entry['id'])
    except ValueError:
        return False
    return True
def deduplicate_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen_ids = set()
    unique_entries = []
    for entry in entries:
        if validate_entry(entry):
            entry_id = str(entry['id'])
            if entry_id not in seen_ids:
                seen_ids.add(entry_id)
                unique_entries.append(entry)
    return unique_entries
def ingest_data(source_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    all_entries = source_list.copy()
    processed_entries = deduplicate_entries(all_entries)
    for entry in processed_entries:
        if not isinstance(entry.get('data'), dict):
            entry['data'] = {}
    return processed_entries
if __name__ == '__main__':
    sample_data_1 = [
        {'id': '001', 'name': 'Alice', 'age': 30, 'data': {'role': 'admin'}},
        {'id': '002', 'name': 'Bob', 'age': 25, 'data': {}},
    ]
    sample_data_2 = [
        {'id': '001', 'name': 'Alice Duplicate', 'age': 31, 'data': {'role': 'user'}},
        {'id': '003', 'name': '', 'age': 40, 'data': {}},
    ]
    combined_data = sample_data_1 + sample_data_2
    final_list = ingest_data(combined_data)
    print(json.dumps(final_list))