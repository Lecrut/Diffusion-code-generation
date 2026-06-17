import threading
from typing import Any, Dict, Callable
class HighPerformanceLookupTable:
    def __init__(self):
        self._lock = threading.Lock()
        self._table: Dict[Any, Any] = {}
    def add_entry(self, key: Any, value: Any) -> None:
        with self._lock:
            if isinstance(key, int):
                self._table[key] = value
            elif isinstance(key, str):
                hashed_key = hash(key) % (10**9 + 7)
                self._table[hashed_key] = key, value
    def get_value(self, key: Any) -> Any:
        with self._lock:
            if isinstance(key, int):
                return self._table.get(key)
            elif isinstance(key, str):
                hashed_key = hash(key) % (10**9 + 7)
                stored_key, value = self._table.get(hashed_key)
                return value if stored_key == key else None
    def get_all(self) -> Dict[Any, Any]:
        with self._lock:
            result = {}
            for k, v in self._table.items():
                if isinstance(k, int):
                    result[k] = v
                elif isinstance(v[0], str):
                    key_val, value = v
                    result[key_val] = value
            return result
def generate_sample_data() -> None:
    table = HighPerformanceLookupTable()
    for i in range(1000):
        table.add_entry(i, f"Value_{i}")
    words = ["apple", "banana", "cherry", "date"]
    indices = [5, 6, 7, 8]
    for w, idx in zip(words, indices):
        table.add_entry(w, f"Fruit_{idx}")
if __name__ == '__main__':
    generate_sample_data()