from typing import Dict, List, Any
def build_dynamic_mapping(data: List[Dict[str, Any]]) -> Dict[Any, int]:
    valid_entries = [entry for entry in data if isinstance(entry.get('value'), (int, float))]
    return {key: len([e for e in valid_entries if e['id'] == key]) 
            for key in set(e['id'] for e in valid_entries)}
if __name__ == '__main__':
    sample_data = [
        {'id': 'user_001', 'value': 10},
        {'id': 'user_002', 'value': 20},
        {'id': 'user_003', 'value': None},
        {'id': 'user_004', 'value': 30.5},
        {'id': 'user_001', 'value': 15}
    ]
    result = build_dynamic_mapping(sample_data)
    print(result)