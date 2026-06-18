import json
from typing import Dict, Any
def build_dictionary(data: list[Dict[str, Any]]) -> Dict[str, int]:
    counter = {}
    for item in data:
        value = str(item.get('value', ''))
        if not isinstance(value, (int, float)):
            try:
                value = json.dumps(value)
            except TypeError:
                pass
        else:
            value = int(value)
        counter[value] = counter.get(value, 0) + 1
    return dict(sorted(counter.items()))
if __name__ == '__main__':
    sample_data = [
        {'value': 'apple'},
        {'value': 'banana'},
        {'value': 'cherry'},
        {'value': 'date'},
        {'value': 'elderberry'}
    ] * 1000
    result_dict = build_dictionary(sample_data)
    print(json.dumps(result_dict, indent=2))