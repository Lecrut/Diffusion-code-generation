import json
def validate_entry(entry):
    required_keys = ['id', 'type', 'properties']
    if not isinstance(entry, dict):
        return False
    for key in required_keys:
        if key not in entry:
            return False
        if key == 'type' and (not isinstance(entry['type'], str) or len(entry['type']) < 1):
            return False
        if key == 'properties':
            if not isinstance(entry['properties'], dict):
                return False
    return True
def process_objects(data_list, parent_key='root'):
    result = {}
    for idx, entry in enumerate(data_list):
        try:
            is_valid = validate_entry(entry)
            if not is_valid:
                error_msg = f"Malformed entry at index {idx}: Missing required keys or invalid structure."
                raise ValueError(error_msg)
            item_id = str(idx + 1).zfill(3)
            nested_structure = {}
            for key, value in entry.items():
                if isinstance(value, dict):
                    child_key = f"{key}_details"
                    nested_structure[child_key] = process_objects([value], parent_key=f"{parent_key}.{item_id}")
                else:
                    nested_structure[key] = value
            result[item_id] = {
                'type': entry['type'],
                **nested_structure,
                '_metadata': {'source_index': idx}
            }
        except ValueError as e:
            print(f"Validation Error: {e}")
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": "obj_01", "type": "vehicle", "properties": {"color": "red"}},
        {"id": "obj_02", "type": "animal", "properties": {}},
        {"invalid_entry": True, "missing_type": False},
        {"id": "", "type": 123, "properties": [1, 2]},
    ]
    organized_data = process_objects(sample_data)
    print(json.dumps(organized_data, indent=4))