import time
class FastDictionary:
    def __init__(self):
        self._data = {}
    def add(self, key, value):
        self._data[key] = value
    def lookup(self, key):
        return self._data.get(key)
    def remove(self, key):
        if key in self._data:
            del self._data[key]
if __name__ == '__main__':
    d = FastDictionary()
    large_data = {f"key_{i}": f"value_{i}" for i in range(1000)}
    start_time = time.time()
    for k, v in large_data.items():
        d.add(k, v)
    add_time = time.time() - start_time
    lookup_keys = ["key_50", "key_999"]
    results = []
    for key in lookup_keys:
        val = d.lookup(key)
        if val is not None:
            results.append(val)
    end_time = time.time()
    print(f"Addition Time: {add_time:.4f}s")
    print(f"Lookup Results: {results}")