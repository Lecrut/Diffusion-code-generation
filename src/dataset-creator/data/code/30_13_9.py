import json
def validate_entry(entry):
    required_keys = ['id', 'type', 'attributes']
    if not isinstance(entry, dict):
        return False
    for key in required_keys:
        if key not in entry:
            return False
        if key == 'id' and (not isinstance(entry['id'], str) or len(entry['id']) == 0):
            return False
        if key == 'type' and (not isinstance(entry['type'], str)):
            return False
        if not isinstance(entry.get('attributes'), dict):
            return False
    return True
def process_objects(data_list, parent_key='root'):
    processed = []
    for index, entry in enumerate(data_list):
        try:
            is_valid = validate_entry(entry)
            if not is_valid:
                raise ValueError(f"Malformed entry at index {index}: Missing required fields or invalid structure.")
            item_node = {
                'id': str(entry['id']),
                'type': entry['type'],
                'attributes': {},
                'children': []
            }
            for attr_key, attr_value in entry.get('attributes', {}).items():
                if not isinstance(attr_value, (str, int, float)):
                    raise ValueError(f"Invalid attribute value type at index {index} key '{attr_key}'.")
                item_node['attributes'][attr_key] = str(attr_value)
            processed.append(item_node)
        except Exception as e:
            print(f"Error processing entry at index {index}: {str(e)}")
    return processed
if __name__ == '__main__':
    sample_data = [
        {'id': 'obj_01', 'type': 'device', 'attributes': {'brand': 'Apple', 'model': 'iPhone 14'}},
        {'id': 'obj_02', 'type': 'software', 'attributes': {'name': 'Python', 'version': '3.9'}},
        {'invalid_entry': True, 'missing_fields': False},
        {'id': '', 'type': 'device', 'attributes': {}},
        {'id': 'obj_04', 'type': 123, 'attributes': {}}
    ]
    try:
        organized_structure = process_objects(sample_data)
        final_output = {parent_key: organized_structure}
        print(json.dumps(final_output, indent=2))
    except Exception as e:
        print(f"Fatal error during processing: {str(e)}")