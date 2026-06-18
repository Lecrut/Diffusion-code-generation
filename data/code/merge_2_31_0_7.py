import time
class FastDictionary:
    def __init__(self):
        self._data = {}
    def lookup(self, key):
        return self._data.get(key)
    def insert(self, key, value):
        self._data[key] = value
if __name__ == '__main__':
    d = FastDictionary()
    sample_data = [
        ("apple", "fruit"),
        ("carrot", "vegetable"),
        ("banana", "fruit"),
        ("book", "object"),
        ("computer", "device")
    ]
    for k, v in sample_data:
        d.insert(k, v)
    start_time = time.time()
    test_keys = ["apple", "carrot", "grape"]                          
    results = []
    for key in test_keys:
        val = d.lookup(key)
        if val is None:
            print(f"Key '{key}' not found.")
        else:
            print(f"Key '{key}': {val}")
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nLookup completed in {duration:.6f} seconds")