import json
def validate_entry(entry):
    required_keys = ['id', 'type', 'properties']
    if not isinstance(entry, dict):
        return False
    for key in required_keys:
        if key not in entry:
            return False
        if key == 'type' and not isinstance(entry['type'], str) or len(entry['type']) < 1:
            return False
        if key == 'properties':
            if not isinstance(entry['properties'], dict):
                return False
    return True
def parse_nested_data(data_list, parent_key=None):
    result = []
    for item in data_list:
        try:
            entry_id = str(item.get('id', ''))[:10]
            if not validate_entry(item):
                raise ValueError(f"Malformed entry at index {data_list.index(item)}")
            nested_obj = {'id': entry_id, 'type': item['type']}
            for prop_key in ['name', 'value']:
                if prop_key in item.get('properties', {}):
                    val = item['properties'][prop_key]
                    try:
                        parsed_val = float(val)
                    except (ValueError, TypeError):
                        pass
                    nested_obj[prop_key] = {
                        'type': str(type(parsed_val).__name__),
                        'value': val if isinstance(val, (int, float)) else None
                    }
            result.append(nested_obj)
        except Exception as e:
            raise ValueError(f"Processing error for entry with id '{item.get('id', '')}': {str(e)}")
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': '001', 'type': 'sensor', 'properties': {'name': 'temp_01', 'value': 25.5}},
        {'id': '002', 'type': 'device', 'properties': {'name': 'cam_main', 'value': 'active'}},
        {'id': 'invalid'},
    ]
    try:
        organized_data = parse_nested_data(sample_data)
        output_structure = {
            "metadata": {"total_entries_processed": len(organized_data)},
            "objects": organized_data,
            "validation_status": "complete" if all(validate_entry(o) for o in organized_data) else "partial_failure"
        }
        print(json.dumps(output_structure, indent=2))
    except ValueError as ve:
        error_report = {
            "error_type": "ValidationException",
            "message": str(ve),
            "action_taken": "entry_rejected_or_skipped"
        }
        print(json.dumps(error_report, indent=2))