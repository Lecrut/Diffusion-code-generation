import hashlib
def validate_and_deduplicate(entries):
    seen_hashes = set()
    unique_entries = []
    for entry in entries:
        if isinstance(entry, dict) and 'id' in entry:
            hash_key = hashlib.sha256(str(entry['id']).encode()).hexdigest()[:10]
        else:
            data_str = str(entry).replace('\n', '')
            hash_key = hashlib.sha256(data_str.encode()).hexdigest()[:10]
        if hash_key not in seen_hashes:
            seen_hashes.add(hash_key)
            unique_entries.append(entry)
    return unique_entries
def ingest_data(source_name, raw_entries):
    validated_list = validate_and_deduplicate(raw_entries)
    print(f"Processed {len(validated_list)} entries from source '{source_name}'")
    for i, item in enumerate(validated_list):
        if isinstance(item, dict):
            print(f"{i+1}: ID={item.get('id', 'N/A')}, Name={item.get('name', 'Unknown')}")
        else:
            print(f"{i+1}: {str(item)}")
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'name': 'Alice'},
        {'id': 102, 'name': 'Bob'},
        {'id': 103, 'name': 'Charlie'},
        {'id': 104, 'name': 'David'},
    ] + [
        {'id': 105, 'name': 'Eve'},
        {'id': 201, 'name': 'Alice Duplicate'},                                                                            
        "String Entry One",
        {"key": "value"},
    ]
    ingest_data("TestSource", sample_data)