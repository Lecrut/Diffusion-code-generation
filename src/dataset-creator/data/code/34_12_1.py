import hashlib
from typing import List, Dict, Any
def validate_entry(entry: Dict[str, Any]) -> bool:
    required_fields = ['id', 'name']
    for field in required_fields:
        if not entry.get(field):
            return False
    try:
        int(entry['id'])
    except (ValueError, TypeError):
        return False
    return True
def deduplicate_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen_ids = set()
    unique_entries = []
    for entry in entries:
        if not validate_entry(entry):
            continue
        id_val = str(entry['id'])
        if id_val not in seen_ids:
            seen_ids.add(id_val)
            unique_entries.append(entry)
    return unique_entries
def ingest_data(source_name: str, raw_entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    validated = [e for e in raw_entries if validate_entry(e)]
    deduped = deduplicate_entries(validated)
    print(f"Processed {source_name}: Validated {len(raw_entries)} entries, kept {len(deduped)}.")
    return deduped
if __name__ == '__main__':
    sample_data_1 = [
        {'id': 101, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 102, 'name': 'Bob', 'email': 'bob@example.com'}
    ]
    sample_data_2 = [
        {'id': 103, 'name': 'Charlie', 'email': 'charlie@example.com'},
        {'id': 101, 'name': 'Alice Duplicate', 'email': 'alice_dup@test.com'}
    ]
    central_list = []
    central_list.extend(ingest_data("Source_A", sample_data_1))
    central_list.extend(ingest_data("Source_B", sample_data_2))
    print(f"Final Centralized List: {central_list}")