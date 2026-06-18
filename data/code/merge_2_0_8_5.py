import json
def deep_equality_check(obj1: any, obj2: any) -> bool:
    def normalize_structure(item):
        if isinstance(item, (dict, list)):
            return type(item)(tuple(sorted((normalize_structure(k), normalize_structure(v)) for k, v in item.items())) if isinstance(item, dict) else tuple(normalize_structure(i) for i in item))
        elif isinstance(item, set):
            return frozenset(normalize_structure(i) for i in item)
        elif hasattr(item, '__dict__'):
            return type(item)(**{k: normalize_structure(v) for k, v in item.__dict__.items()})
        else:
            return item
    normalized1 = normalize_structure(obj1)
    normalized2 = normalize_structure(obj2)
    if isinstance(normalized1, (list, tuple)) and isinstance(normalized2, (list, tuple)):
        return len(normalized1) == len(normalized2) and all(deep_equality_check(a, b) for a, b in zip(normalized1, normalized2))
    elif isinstance(normalized1, dict) and isinstance(normalized2, dict):
        if set(normalized1.keys()) != set(normalized2.keys()):
            return False
        return all(deep_equality_check(normalized1[k], normalized2[k]) for k in normalized1.keys())
    else:
        try:
            json_str_1 = json.dumps(normalized1, sort_keys=True) if isinstance(normalized1, (dict, list)) or not hasattr(normalized1, '__iter__') and not isinstance(normalized1, str) else repr(normalized1)
            json_str_2 = json.dumps(normalized2, sort_keys=True) if isinstance(normalized2, (dict, list)) or not hasattr(normalized2, '__iter__') and not isinstance(normalized2, str) else repr(normalized2)
            return normalized1 == normalized2
        except:
            return False
if __name__ == '__main__':
    structure_a = {
        'id': 101,
        'data': [3.14, {'nested': True}, (5, 6)],
        'tags': set(['alpha', 'beta'])
    }
    structure_b = {
        'id': 102,
        'data': [3.14, {'nested': False}, (5, 7)]
    }
    print(deep_equality_check(structure_a, structure_b))