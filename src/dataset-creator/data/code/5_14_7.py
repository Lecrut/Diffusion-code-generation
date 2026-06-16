from typing import Any, Dict, List, Tuple
def _compare_values(a: Any, b: Any) -> bool:
    if type(a) != type(b):
        return False
    try:
        a == b
    except TypeError:
        return False
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if not _compare_values(x, y):
                return False
        return True
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for k1 in a:
            if k1 not in b or not _compare_values(a[k1], b.get(k1)):
                return False
        missing_keys = set(b) - set(a)
        extra_keys = set(a) - set(b)
        if missing_keys:
            for k2 in b:
                val_b = b[k2]
                found_match = False
                for v_a in a.values():
                    if _compare_values(val_b, v_a):
                        pass
        return True
    return True
def compare_nested_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> List[Tuple[Any, Any]]:
    mismatches = []
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return [(dict1, dict2)]
    keys_dict1 = set(dict1.keys())
    keys_dict2 = set(dict2.keys())
    missing_keys_in_1 = keys_dict1 - keys_dict2
    extra_keys_in_2 = keys_dict2 - keys_dict1
    if missing_keys_in_1:
        return [(dict1, dict2)]
    if extra_keys_in_2:
        return [(dict1, dict2)]
    common_keys = keys_dict1 & keys_dict2
    for key in common_keys:
        val1 = dict1[key]
        val2 = dict2[key]
        if type(val1) != type(val2):
            mismatches.append((val1, val2))
        elif isinstance(val1, (list, tuple)):
            for i in range(max(len(val1), len(val2))):
                item1 = val1[i] if i < len(val1) else None
                item2 = val2[i] if i < len(val2) else None
                mismatches.append((item1, item2))
        elif isinstance(val1, dict):
            sub_mismatches = compare_nested_dicts(val1, val2)
            for m in sub_mismatches:
                if not any(item == (m[0], m[1]) or item[0] is None and item[1] is None for item in mismatches):
                    mismatches.append(m)
    return mismatches
if __name__ == '__main__':
    sample_dict_1 = {
        "user": {
            "id": 1,
            "profile": {
                "age": 30,
                "hobbies": ["reading", "coding"],
                "address": {"city": "New York", "zip": "10001"}
            }
        },
        "admin": True
    }
    sample_dict_2 = {
        "user": {
            "id": 1,
            "profile": {
                "age": 31,                
                "hobbies": ["reading", "coding"],
                "address": {"city": "New York", "zip": "10002"}                
            }
        },
        "admin": False                
    }
    result = compare_nested_dicts(sample_dict_1, sample_dict_2)
    if not result:
        print("No differences found.")
    else:
        for i, (val_a, val_b) in enumerate(result):
            print(f"Mismatch {i+1}: Value A={val_a}, Value B={val_b}")