import json
def validate_entry(entry):
    required_keys = ['id', 'type', 'properties']
    if not isinstance(entry, dict):
        return False
    for key in required_keys:
        if key not in entry:
            return False
        prop_val = entry.get(key)
        if key == 'id':
            if not isinstance(prop_val, (int, str)):
                raise ValueError(f"Invalid id type. Expected int or str, got {type(prop_val).__name__}")
        elif key == 'type':
            valid_types = ['car', 'person', 'animal']
            if prop_val not in valid_types:
                raise ValueError(f"Invalid object type '{prop_val}'. Must be one of {valid_types}")
        else:
            if not isinstance(prop_val, dict):
                raise ValueError(f"'{key}' must be a dictionary")
def organize_data(entries):
    organized = {'objects': []}
    for idx, entry in enumerate(entries):
        try:
            validate_entry(entry)
            obj_record = {
                'id': str(idx + 1),
                'type': entry['type'],
                'properties': {}
            }
            if 'name' in entry and isinstance(entry['name'], str):
                obj_record['properties']['name'] = entry['name']
            if 'color' in entry:
                color_val = entry['color']
                if not isinstance(color_val, (str, int)):
                    raise ValueError(f"Invalid color type. Expected string or int")
                obj_record['properties']['color'] = str(color_val)
            organized['objects'].append(obj_record)
        except Exception as e:
            error_msg = f"Error processing entry {idx}: {str(e)}"
            print(error_msg)
if __name__ == '__main__':
    sample_entries = [
        {'id': 101, 'type': 'car', 'properties': {}},
        {'id': "2", 'type': 'person', 'properties': {'name': 'Alice'}},
        {'id': 3.5, 'type': 'animal'},
        {'id': 4, 'type': 'unknown_type', 'properties': {'color': 'red'}}
    ]
    organize_data(sample_entries)