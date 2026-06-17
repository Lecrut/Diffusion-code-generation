import threading
from collections import OrderedDict
from typing import Any, Dict, List, Tuple
class BulkDictionary:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
        self._integrity_status = "OK"
    def bulk_insert(self, items: List[Tuple[Any, Any]]) -> int:
        count = 0
        with self._lock:
            for key, value in items:
                if isinstance(key, (list, tuple)) and len(key) == 2:
                    k, v = key[0], key[1]
                else:
                    k, v = key, value
                try:
                    self._data[k] = v
                    count += 1
                except TypeError:
                    pass
        return count
    def get(self, key: Any) -> Any:
        with self._lock:
            if isinstance(key, (list, tuple)) and len(key) == 2:
                k, _ = key[0], key[1]
            else:
                k = key
            return self._data.get(k)
    def delete(self, key: Any) -> bool:
        with self._lock:
            if isinstance(key, (list, tuple)) and len(key) == 2:
                k, _ = key[0], key[1]
            else:
                k = key
            return self._data.pop(k, None) is not None
    def get_integrity_status(self) -> str:
        with self._lock:
            missing_keys_count = 0
            for item in list(self._data.items()):
                if isinstance(item[0], (list, tuple)) and len(item[0]) == 2:
                    k, v = item[0][0], item[0][1]
                else:
                    k, v = item[0], item[1]
                try:
                    self._data[k]
                except TypeError:
                    missing_keys_count += 1
            if missing_keys_count > 0:
                return f"WARNING: {missing_keys_count} potential integrity issues detected in table structure."
            return "OK"
if __name__ == '__main__':
    db = BulkDictionary()
    sample_data = [
        ("apple", "fruit"),
        (["banana"], ["yellow"]),
        ((1, 2), {"x": 5}),
        ("cherry", None)
    ]
    inserted_count = db.bulk_insert(sample_data)
    print(f"Successfully inserted {inserted_count} items.")
    status = db.get_integrity_status()
    print(status)
    retrieved_value = db.get(("apple", "fruit"))
    if isinstance(retrieved_value, dict):
        print("Retrieved value:", retrieved_value)