import threading
from typing import Any, Dict, Callable
class HighPerformanceLookupTable:
    def __init__(self):
        self._data: Dict[Any, Any] = {}
        self._lock = threading.Lock()
    def add(self, key: Any, value: Any) -> None:
        with self._lock:
            if key in self._data:
                raise ValueError(f"Key {key} already exists")
            self._data[key] = value
    def get(self, key: Any) -> Any:
        return self._data.get(key)
def generate_sample_data() -> None:
    table = HighPerformanceLookupTable()
    test_keys = [1001, "alpha", 3.14, True]
    test_values = ["One Hundred One", "Alpha Symbol", "Pi Value", "Boolean True"]
    zip_data = list(zip(test_keys, test_values))
    for key, value in zip_data:
        table.add(key, value)
if __name__ == '__main__':
    generate_sample_data()