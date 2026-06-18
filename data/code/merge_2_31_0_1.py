import time
from collections import defaultdict
class FastDictionary:
    def __init__(self):
        self.data = {}
    def add(self, key, value):
        self.data[key] = value
    def lookup(self, key):
        return self.data.get(key)
    def remove(self, key):
        if key in self.data:
            del self.data[key]
if __name__ == '__main__':
    d = FastDictionary()
    sample_data = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3),
        ("date", 4)
    ]
    for k, v in sample_data:
        d.add(k, v)
    start_time = time.time()
    results = []
    for key in ["apple", "banana", "nonexistent"]:
        val = d.lookup(key)
        if val is not None:
            results.append(val)
    end_time = time.time()
    print(f"Lookup Results: {results}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
if __name__ == '__main__':
    d2 = FastDictionary()
    large_dataset = [(i, i*i) for i in range(1000)]
    for item in large_dataset:
        d2.add(item[0], item[1])
    start_time = time.time()
    target_key = 500
    result = d2.lookup(target_key)
    end_time = time.time()
    print(f"Key {target_key} -> Value {result}")