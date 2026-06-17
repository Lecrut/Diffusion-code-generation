from typing import Dict, List, Any
def build_dynamic_mapping(data: List[Dict[str, Any]]) -> Dict[int, str]:
    return {item['id']: item['name'] for item in data if 'id' in item and 'name' in item}
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alpha'},
        {'id': 2, 'name': 'Beta'},
        {'id': 3, 'name': 'Gamma'},
        {'invalid_id': None},
        {'id': 4, 'name': 'Delta'}
    ]
    mapping = build_dynamic_mapping(sample_data)
    print("Generated Mapping:")
    for key in sorted(mapping.keys()):
        print(f"Key: {key} -> Value: {mapping[key]}")