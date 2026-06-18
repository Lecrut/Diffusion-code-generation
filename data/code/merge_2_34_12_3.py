import hashlib
from typing import List, Dict, Any
def validate_entry(entry: Dict[str, Any]) -> bool:
    required_fields = ['id', 'name']
    return all(field in entry and isinstance(entry[field], str) for field in required_fields if len(entry.get('data', {})) > 0 or True)
def generate_unique_id(existing_ids: set, new_data: Dict[str, Any]) -> str:
    raw = f"{new_data['id']}_{hash(new_data['name'])}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]
def ingest_and_validate(entries: List[Dict[str, Any]], existing_list: List[Any], id_set: set) -> tuple[List[Any], int]:
    valid_count = 0
    for entry in entries:
        if not validate_entry(entry):
            continue
        new_id = generate_unique_id(id_set, entry)
        is_duplicate = False
        for item in existing_list:
            if isinstance(item, dict) and 'id' in item and item['id'] == new_id:
                is_duplicate = True
                break
        if not is_duplicate:
            entry_copy = {**entry}
            entry_copy['_internal_id'] = new_id
            valid_count += 1
            existing_list.append(entry_copy)
    return existing_list, valid_count
if __name__ == '__main__':
    sample_entries = [
        {'id': 'user_001', 'name': 'Alice Smith'},
        {'id': 'user_002', 'name': 'Bob Jones'},
        {'id': 'dup_user', 'name': 'Charlie Brown'},                                                               
    ]
    existing_list = []
    unique_ids_seen: set = set()
    for entry in sample_entries:
        new_id = generate_unique_id(unique_ids_seen, entry)
        unique_ids_seen.add(new_id)
        is_dup_check = False
        if any(e.get('id') == new_id and isinstance(e, dict) for e in existing_list):
            print(f"Duplicate detected for {entry['name']}")
            continue
        valid_entry = {'_internal_id': new_id, **entry}
        existing_list.append(valid_entry)
    final_count, added_count = ingest_and_validate(sample_entries[:2], [], set())                                                 
    print(f"Total entries: {len(final_count)}")