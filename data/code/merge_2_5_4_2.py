import threading
from typing import Any, Dict, List
class ThreadSafeDictComparator:
    def __init__(self):
        self.lock = threading.Lock()
    def compare_dicts(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> bool:
        with self.lock:
            return self._dfs_compare(dict_a, dict_b)
    def _dfs_compare(self, node_a: Any, node_b: Any) -> bool:
        if type(node_a) != type(node_b):
            return False
        if isinstance(node_a, dict):
            if len(node_a) != len(node_b):
                return False
            for key in node_a:
                if key not in node_b or not self._dfs_compare(node_a[key], node_b[key]):
                    return False
            return True
        elif isinstance(node_a, list):
            if len(node_a) != len(node_b):
                return False
            for i in range(len(node_a)):
                if not self._dfs_compare(node_a[i], node_b[i]):
                    return False
            return True
        else:
            return node_a == node_b
def main():
    comparator = ThreadSafeDictComparator()
    dict_one = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10001"
        },
        "hobbies": ["reading", "coding"]
    }
    dict_two = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10002"
        },
        "hobbies": ["reading", "coding"]
    }
    dict_three = {
        "name": "Bob",
        "age": 30,
        "address": {
            "city": "New York",
            "zip_code": "10001"
        },
        "hobbies": ["reading"]
    }
    result_one = comparator.compare_dicts(dict_one, dict_two)
    result_two = comparator.compare_dicts(dict_one, dict_three)
    print(f"Dictionaries 1 and 2 are equal: {result_one}")
    print(f"Dictionaries 1 and 3 are equal: {result_two}")
if __name__ == '__main__':
    main()