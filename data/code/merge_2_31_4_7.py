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
    numeric_keys = [100, 205.5, -34]
    string_keys = ["alpha", "beta_99", "gamma"]
    complex_objects = {"id": 789}
    table.add(100, "Primary Node")
    table.add(205.5, "Secondary Cluster")
    table.add(-34, "Tertiary Region")
    for key in string_keys:
        table.add(key, f"Config_{key}")
    try:
        table.add(complex_objects["id"], {"status": "active", "priority": 1})
    except Exception:
        pass
if __name__ == '__main__':
    generate_sample_data()