import json
from typing import Dict, Any, List
def build_high_performance_dict(data: List[Dict[str, Any]]) -> Dict[Any, Any]:
    result = {}
    for item in data:
        key = id(item) if isinstance(item, dict) else str(id(item))
        value = json.dumps(item)
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "value": "alpha"},
        {"id": 2, "value": "beta"},
        {"id": 3, "value": "gamma"}
    ]
    output_dict = build_high_performance_dict(sample_data)
    print(json.dumps(output_dict))