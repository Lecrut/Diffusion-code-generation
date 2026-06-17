import json
class DataValidationError(Exception):
    pass
def validate_object(entry: dict) -> bool:
    if not isinstance(entry, dict):
        return False
    required_keys = ['id', 'name']
    for key in required_keys:
        if key not in entry or not isinstance(entry[key], str):
            raise DataValidationError(f"Malformed entry at index {list(entry.keys())}: missing or invalid string type for '{key}'")
    return True
def organize_data(raw_entries: list) -> dict:
    validated_structure = {'objects': []}
    try:
        if not isinstance(raw_entries, list):
            raise DataValidationError("Input must be a list of object dictionaries.")
        for idx, entry in enumerate(raw_entries):
            validate_object(entry)
            category = 'default'
            name_val = entry.get('name', '')
            if len(name_val) > 5:
                category = 'large_name'
            validated_structure['objects'].append({
                'id': str(idx),
                'category': category,
                'data': {k: v for k, v in entry.items() if k not in ['name']}
            })
    except DataValidationError as e:
        raise ValueError(f"Validation failed during data organization: {str(e)}")
def main():
    sample_data = [
        {'id': '001', 'name': 'Apple'},
        {'id': '002', 'name': 'Banana'} , 
        {'id': 'invalid_id', 'name': 123},
        {'id': '004', 'name': 'Carrot'},
    ]
    try:
        organized = organize_data(sample_data)
        print(json.dumps(organized, indent=2))
    except ValueError as ve:
        print(f"Error processing data: {ve}")
if __name__ == '__main__':
    main()