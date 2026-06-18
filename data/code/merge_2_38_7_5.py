from typing import Dict, List, Any
def build_dynamic_mapping(data: List[Dict[str, Any]]) -> Dict[Any, int]:
    valid_entries = [entry for entry in data if isinstance(entry.get('value'), (int, float))]
    return {key: len([e for e in valid_entries if e['id'] == key]) 
            for key in set(e['id'] for e in valid_entries)}
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': None},
        {'id': 4, 'value': 40.5},
        {'id': 1, 'value': 15}
    ]
    result = build_dynamic_mapping(sample_data)
    print(result)