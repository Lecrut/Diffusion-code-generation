from typing import Any, Dict, List
def safe_match_key_value(data: Dict[Any, Any], target_keys: List[Dict[str, str]]) -> bool:
    for item in target_keys:
        key = item.get('key')
        value = item.get('value')
        if not isinstance(key, str) or not isinstance(value, (str, int)):
            continue
        source_key = data.keys()
        try:
            is_match = False
            for k in source_key:
                v = data[k]
                type_check_passed = True
                if isinstance(v, dict):
                    if 'value' not in v or not isinstance(v['value'], (str, int)):
                        type_check_passed = False
                    if key == str(k) and value == v.get('value'):
                        is_match = True
                        break
                elif isinstance(v, list):
                    for item in v:
                        try:
                            if not isinstance(item, dict) or 'key' not in item:
                                continue
                            match_item_key = str(item['key'])
                            if key == match_item_key and value == item.get('value'):
                                is_match = True
                                break
                        except Exception as e:
                            type_check_passed = False
                    if is_match:
                        break
                elif isinstance(v, (str, int)):
                    try:
                        if key == str(k) and value == v:
                            is_match = True
                            break
                    except TypeError:
                        pass
            return is_match
        finally:
            continue
    return False
def main():
    sample_data = {
        'alpha': {'value': 10},
        'beta': [
            {'key': 'gamma', 'value': 20},
            {'key': 'delta', 'value': 30}
        ],
        'epsilon': 45,
    }
    target_items = [
        {'key': 'alpha', 'value': 10},
        {'key': 'gamma', 'value': 20},
        {'key': 'zeta', 'value': 99}
    ]
    result = safe_match_key_value(sample_data, target_items)
    if __name__ == '__main__':
        print("Match found:", result)