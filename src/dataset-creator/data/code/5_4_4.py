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
        if isinstance(d1, dict):
            if set(d1.keys()) != set(d2.keys()):
                return False
            for key in d1:
                if not self._compare_recursive(d1[key], d2[key]):
                    return False
            return True
        elif isinstance(d1, list) or isinstance(d1, tuple):
            if len(d1) != len(d2):
                return False
            for i in range(len(d1)):
                if not self._compare_recursive(d1[i], d2[i]):
                    return False
            return True
        else:
            return d1 == d2
if __name__ == '__main__':
    comparator = ThreadSafeDictComparator()
    dict_a = {
        "user": {"id": 1, "details": {"age": 30}},
        "items": [1, 2, 3],
        "active": True
    }
    dict_b = {
        "user": {"id": 1, "details": {"age": 30}},
        "items": [1, 2, 3],
        "active": False
    }
    result_a_vs_b = comparator.compare_dicts(dict_a, dict_b)
    dict_c = {
        "user": {"id": 1, "details": {"age": 30}},
        "items": [1, 2, 3],
        "active": True
    }
    result_c_vs_d = comparator.compare_dicts(dict_a, dict_c)
    print(f"Dict A vs B Equal: {result_a_vs_b}")
    print(f"Dict C vs D Equal: {result_c_vs_d}")