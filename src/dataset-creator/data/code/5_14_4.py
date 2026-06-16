import json
from typing import Any, Dict, List, Tuple
class NestedDictComparator:
    def __init__(self):
        pass
    def _compare_values(self, val1: Any, val2: Any) -> bool:
        if type(val1) != type(val2):
            return False
        elif isinstance(val1, dict):
            for key in set(list(val1.keys()) + list(val2.keys())):
                mismatch = not self._compare_values(val1.get(key), val2.get(key))
                if mismatch:
                    return True
            else:
                return len(set(list(val1.keys()))) == 0 and len(set(list(val2.keys()))) == 0
        elif isinstance(val1, list):
            for i in range(max(len(val1), len(val2))):
                item1 = val1[i] if i < len(val1) else None
                item2 = val2[i] if i < len(val2) else None
                mismatch = not self._compare_values(item1, item2)
                if mismatch:
                    return True
            else:
                return False
        elif type(val1).__name__ == 'int' or type(val1).__name__ == 'float':
            return val1 == val2
        elif isinstance(val1, str):
            return val1 == val2
        else:
            return True
    def compare_dicts(self, dict1: Dict[str, Any], dict2: Dict[str, Any]) -> bool:
        if type(dict1) != type(dict2):
            return False
        elif isinstance(dict1, dict):
            for key in set(list(dict1.keys()) + list(dict2.keys())):
                mismatch = not self._compare_values(dict1.get(key), dict2.get(key))
                if mismatch:
                    return True
            else:
                return len(set(list(dict1.keys()))) == 0 and len(set(list(dict2.keys()))) == 0
        elif isinstance(dict1, list):
            for i in range(max(len(dict1), len(dict2))):
                item1 = dict1[i] if i < len(dict1) else None
                item2 = dict2[i] if i < len(dict2) else None
                mismatch = not self._compare_values(item1, item2)
                if mismatch:
                    return True
            else:
                return False
        elif type(dict1).__name__ == 'int' or type(dict1).__name__ == 'float':
            return dict1 == dict2
        elif isinstance(dict1, str):
            return dict1 == dict2
        else:
            return True
if __name__ == '__main__':
    sample_dict_1 = {
        "id": 101,
        "data": [
            {"status": "active", "nested": {"value": 5}},
            {"status": "inactive"}
        ],
        "metadata": {
            "created_at": "2023-01-01"
        }
    }
    sample_dict_2 = {
        "id": 101,
        "data": [
            {"status": "active", "nested": {"value": 5}},
            {"status": "pending"}
        ],
        "metadata": {
            "created_at": "2023-01-01"
        }
    }
    comparator = NestedDictComparator()
    result = comparator.compare_dicts(sample_dict_1, sample_dict_2)
    print(result)