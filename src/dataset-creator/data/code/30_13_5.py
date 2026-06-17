import json
def validate_entry(entry):
    required_keys = ['id', 'type']
    for key in required_keys:
        if not isinstance(entry.get(key), str) or entry[key] == "":
            raise ValueError(f"Malformed entry at index {entry.get('index')}: missing or invalid '{key}' field.")
    optional_types = {'car', 'person'}
    if entry['type'] not in optional_types:
        raise ValueError(f"Invalid type '{entry['type']}' for entry at index {entry.get('index')}")
def organize_objects(entries):
    organized_data = {"objects": []}
    try:
        for idx, item in enumerate(entries):
            validate_entry(item)
            obj_record = {}
            if 'name' in item and isinstance(item['name'], str):
                obj_record["attributes"] = {"name": item['name']}
            if 'color' in item and isinstance(item['color'], str):
                obj_record["attributes"]["color"] = item['color']
            if 'age' in item:
                try:
                    age_val = int(item['age'])
                    if age_val < 0:
                        raise ValueError("Age cannot be negative")
                    obj_record["attributes"]["age"] = age_val
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Invalid or malformed 'age' value at index {idx}: {e}")
            organized_data["objects"].append(obj_record)
    except Exception as validation_error:
        print(f"[ERROR] Data processing failed due to invalid input structure:")
        print(json.dumps({f"error": str(validation_error), "processed_count": len(organized_data['objects'])}, indent=2))
        raise
    return organized_data
if __name__ == '__main__':
    sample_entries = [
        {"id": 101, "type": "car", "name": "Sedan", "color": "Red"},
        {"id": 102, "type": "person", "age": 30},
        {"id": 103, "type": "invalid_type", "name": "Unknown"},
        {"id": 104, "type": "car", "color": "Blue"}
    ]
    try:
        result = organize_objects(sample_entries)
        print("\n[SUCCESS] Organized Data Structure:")
        print(json.dumps(result, indent=2))
    except ValueError as ve:
        print(f"\n[CATCHED ERROR]: {ve}")