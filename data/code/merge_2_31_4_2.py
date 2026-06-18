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
    numeric_keys = [100, 205.5, -37]
    string_keys = ["alpha", "beta_99", "gamma"]
    complex_objects = {"id": 42}
    table.add(100, "Primary Node")
    table.add(205.5, "Secondary Cluster")
    table.add(-37, "Backup Server")
    for s in string_keys:
        table.add(s, f"Config_{s}")
    id_key = complex_objects["id"]
    table.add(id_key, {"status": "active", "priority": 1})
if __name__ == '__main__':
    generate_sample_data()