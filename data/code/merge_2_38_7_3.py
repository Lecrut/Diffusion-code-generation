from typing import Dict, List, Any
def build_dynamic_mapping(data: List[Dict[str, Any]]) -> Dict[Any, int]:
    return {item['id']: item['value'] for item in data}
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'value': 'alpha'},
        {'id': 202, 'value': 'beta'},
        {'id': 303, 'value': 'gamma'}
    ]
    mapping: Dict[Any, int] = build_dynamic_mapping(sample_data)
    print(mapping)