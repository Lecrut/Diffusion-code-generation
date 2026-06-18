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
                for key in d1:
                    if key not in d2 or not self._compare_recursive(d1[key], d2.get(key)):
                        return False
                for key in d2:
                    if key not in d1:
                        return False
            elif isinstance(d1, list):
                if len(d1) != len(d2):
                    return False
                for i in range(len(d1)):
                    if not self._compare_recursive(d1[i], d2[i]):
                        return False
        else:
            return d1 == d2
        return True
if __name__ == '__main__':
    dict_a = {
        "user": {"id": 1, "profile": {"age": 30}},
        "items": [1, 2, 3],
        "metadata": None
    }
    dict_b = {
        "user": {"id": 1, "profile": {"age": 30}},
        "items": [1, 2, 3],
        "metadata": None
    }
    comparator = ThreadSafeDictComparator()
    result_a_equal_b = comparator.compare_dicts(dict_a, dict_b)
    print(f"Comparison Result: {result_a_equal_b}")