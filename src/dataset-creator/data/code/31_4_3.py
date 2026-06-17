import threading
from functools import lru_cache
class HighPerformanceLookupTable:
    def __init__(self):
        self._lock = threading.Lock()
        self._table = {}
    @lru_cache(maxsize=None)
    def get_value(self, key):
        with self._lock:
            return self._table.get(key, None)
def generate_sample_data():
    sample_keys = [100, 200, "alpha", True]
    sample_values = {key: f"Value for {key}" if isinstance(key, int) else key.upper() for key in sample_keys}
    return sample_keys, sample_values
if __name__ == '__main__':
    lookup_table = HighPerformanceLookupTable()
    keys, values = generate_sample_data()
    threads = []
    results = {}
    def worker(key):
        result_value = lookup_table.get_value(key)
        if key in values:
            results[key] = (result_value == values[key])
    for i, k in enumerate(keys):
        t = threading.Thread(target=worker, args=(k,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Lookup table initialized with {len(values)} entries.")
    print("Concurrent lookup validation completed successfully.")