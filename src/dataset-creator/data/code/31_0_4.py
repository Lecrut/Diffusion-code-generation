import time
class FastDictionary:
    def __init__(self):
        self._data = {}
    def lookup(self, key):
        return self._data.get(key)
    def add_entry(self, key, value):
        self._data[key] = value
if __name__ == '__main__':
    d = FastDictionary()
    sample_data = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3),
        ("date", 4),
        ("elderberry", 5)
    ]
    for k, v in sample_data:
        d.add_entry(k, v)
    start_time = time.time()
    test_keys = ["apple", "banana", "cherry", "grape", None]
    results = []
    for key in test_keys:
        val = d.lookup(key)
        results.append(val)
    end_time = time.time()
    print("Lookup Results:", results)
    print(f"Time taken: {end_time - start_time:.6f} seconds")