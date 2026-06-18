import json
def validate_entry(entry):
    required_keys = ['id', 'type', 'properties']
    if not isinstance(entry, dict):
        return False
    for key in required_keys:
        if key not in entry:
            return False
        if key == 'id' and (not isinstance(entry['id'], str) or len(entry['id']) < 1):
            return False
        if key == 'type' and (not isinstance(entry['type'], str)):
            return False
        if not isinstance(entry.get('properties'), dict):
            return False
    return True
def process_objects(data_list):
    organized_data = {'objects': []}
    for index, entry in enumerate(data_list):
        if validate_entry(entry):
            try:
                properties_dict = {}
                for prop_key, prop_value in entry['properties'].items():
                    if isinstance(prop_value, (int, float)):
                        properties_dict[prop_key] = round(float(prop_value), 2)
                    elif isinstance(prop_value, str):
                        properties_dict[prop_key] = prop_value.strip()
                organized_data['objects'].append({
                    'id': entry['id'],
                    'type': entry['type'],
                    'properties': properties_dict
                })
            except Exception as e:
                print(f"Error processing object {index}: {str(e)}")
        else:
            error_msg = f"Invalid entry at index {index}"
            if not isinstance(entry, dict):
                error_msg += " - Expected dictionary."
            elif 'id' not in entry:
                error_msg += " Missing required key 'id'."
            elif 'type' not in entry:
                error_msg += " Missing required key 'type'."
            else:
                if isinstance(entry['properties'], dict):
                    missing_props = []
                    for prop_key, _ in entry['properties'].items():
                        try:
                            float(prop_value)
                        except (ValueError, TypeError):
                            pass
                    error_msg += f" Malformed properties at index {index}."
            print(error_msg)
if __name__ == '__main__':
    sample_data = [
        {'id': 'obj_01', 'type': 'vehicle', 'properties': {'speed': 60, 'color': 'red'}},
        {'id': 'obj_02', 'type': 'animal', 'properties': {'weight': 5.5}},
        {'invalid_entry'},
        {'id': '', 'type': 'object', 'properties': {}},
        {'id': 'obj_04', 'type': 'machine', 'properties': {'temp': -10, 'status': 'active'}},
    ]
    try:
        result = process_objects(sample_data)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Fatal error during processing: {str(e)}")