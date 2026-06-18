import json
def validate_object(entry):
    if not isinstance(entry, dict):
        return False
    required_keys = ['id', 'name']
    for key in required_keys:
        if key not in entry:
            return False
        if not isinstance(entry[key], str) or len(str(entry[key])) == 0:
            return False
    try:
        int_val = int(entry.get('category'))
        if not isinstance(int_val, (int, float)):
            raise ValueError("Invalid category type")
    except (ValueError, TypeError):
        return False
    return True
def organize_data(entries):
    organized_structure = {
        'metadata': {'version': 1.0, 'source': 'script'},
        'objects': []
    }
    for index, entry in enumerate(entries):
        if not validate_object(entry):
            continue
        try:
            object_data = {
                'id': str(entry['id']).strip(),
                'name': str(entry['name']).strip(),
                'category': int(entry.get('category', 0)),
                'metadata': entry.get('extra_info') or {}
            }
            organized_structure['objects'].append(object_data)
        except Exception as e:
            pass
    return json.dumps(organized_structure, indent=2)
if __name__ == '__main__':
    sample_entries = [
        {'id': 'obj_001', 'name': 'Apple', 'category': 1},
        {'id': 'obj_002', 'name': 'Banana'},
        {'invalid_entry': True, 'missing_required_keys': []},
        {'id': '', 'name': ''},
        {'id': 'obj_003', 'name': 'Carrot', 'category': 1.5}
    ]
    try:
        result = organize_data(sample_entries)
        print(result)
    except Exception as e:
        error_message = f"System Error: {str(e)}\nFailed to process input data."
        raise RuntimeError(error_message) from None