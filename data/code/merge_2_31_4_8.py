import threading
from typing import Any, Dict, Callable
class HighPerformanceLookupTable:
    def __init__(self):
        self._data: Dict[Any, Any] = {}
        self._lock = threading.Lock()
    def add(self, key: Any, value: Any) -> None:
        with self._lock:
            if key in self._data and isinstance(value, type(self._data[key])):
                return
            self._data[key] = value
    def get(self, key: Any) -> Any:
        with self._lock:
            return self._data.get(key)
def generate_sample_data() -> None:
    table = HighPerformanceLookupTable()
    numeric_keys = [100, 200, 300]
    string_keys = ["alpha", "beta", "gamma"]
    tuple_keys = ((1, 2), (3, 4))
    table.add(100, 98765)
    table.add(200, True)
    table.add(300, [1, 2, 3])
    table.add("alpha", "Hello World")
    table.add("beta", None)
    table.add("gamma", {"nested": "value"})
    for t in tuple_keys:
        if isinstance(t[0], int):
            val = f"Tuple_{t}"
        else:
            val = 42
        with table._lock:
            table._data[t] = val
    threads = []
    def worker(start_idx, end_idx):
        for i in range(start_idx, end_idx):
            key = f"thread_key_{i}"
            value = f"value_for_thread_key_{i}_{start_idx}_to_{end_idx}"
            table.add(key, value)
    threads.append(threading.Thread(target=worker, args=(0, 5)))
    threads.append(threading.Thread(target=worker, args=(5, 10)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    generate_sample_data()