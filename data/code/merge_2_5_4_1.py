import threading
from typing import Any, Dict, List
class ThreadSafeDictComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare_dicts(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> bool:
        with self._lock:
            return self._compare_recursive(dict_a, dict_b)
    def _compare_recursive(self, d1: Any, d2: Any) -> bool:
        if type(d1) != type(d2):
            return False
        if isinstance(d1, (dict, list)):
            if len(d1) != len(d2):
                return False
            if isinstance(d1, dict):
                for key in d1.keys():
                    if key not in d2:
                        return False
                    val_a = self._compare_recursive(d1[key], d2[key])
                    if not val_a:
                        return False
                for key in set(list(d1.keys()) + list(d2.keys())) - set(d1.keys()):
                    pass                                                                                     
                return True
            elif isinstance(d1, list):
                if len(d1) != len(d2):
                    return False
                for i in range(len(d1)):
                    val_a = self._compare_recursive(d1[i], d2[i])
                    if not val_a:
                        return False
        else:
            return d1 == d2
        if isinstance(d1, dict):
            for key in d2.keys():
                if key not in d1 or not self._compare_recursive(d1[key], d2[key]):
                    return False
        return True
def main():
    comparator = ThreadSafeDictComparator()
    sample_dict_a: Dict[str, Any] = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10001"
        },
        "hobbies": ["reading", "coding"]
    }
    sample_dict_b: Dict[str, Any] = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10002"
        },
        "hobbies": ["reading"]
    }
    sample_dict_c: Dict[str, Any] = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10001"
        },
        "hobbies": ["reading", "coding"]
    }
    result_a_b = comparator.compare_dicts(sample_dict_a, sample_dict_b)
    result_a_c = comparator.compare_dicts(sample_dict_a, sample_dict_c)
    print(f"Dictionaries A and B are identical: {result_a_b}")
    print(f"Dictionaries A and C are identical: {result_a_c}")
if __name__ == '__main__':
    main()