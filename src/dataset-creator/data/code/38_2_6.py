import json
from typing import Dict, Any, List
def build_high_performance_dict(data: List[Dict[str, Any]]) -> Dict[Any, int]:
    result = {}
    for item in data:
        value = item.get('value') if isinstance(item, dict) else item
        key_type = type(value).__name__
        raw_key = str(key_type).lower() + "_" + repr(value)[:10]
        result[raw_key] = result.get(raw_key, 0) + 1
    return result
if __name__ == '__main__':
    sample_data: List[Dict[str, Any]] = [
        {'value': 'apple'},
        {'value': 'banana', 'extra': True},
        {'value': 'apple'},
        {'value': None},
        {'value': 42},
        {'value': 'cherry'}
    ]
    output_dict: Dict[Any, int] = build_high_performance_dict(sample_data)
    print(json.dumps(output_dict))