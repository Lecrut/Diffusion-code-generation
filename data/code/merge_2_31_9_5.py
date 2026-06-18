import hashlib
from collections import defaultdict
class BatchKeyMatcher:
    def __init__(self):
        self.index = {}                                                                       
    def add(self, key, value):
        h = int(hashlib.md5(str(key).encode()).hexdigest(), base=16) % (2**32)
        if h not in self.index:
            self.index[h] = []
        self.index[h].append((key, value))
    def lookup(self, key):
        h = int(hashlib.md5(str(key).encode()).hexdigest(), base=16) % (2**32)
        if h not in self.index:
            return None
        for k, v in self.index[h]:
            if k == key:
                return v
        return None
if __name__ == '__main__':
    matcher = BatchKeyMatcher()
    data_points = [f"key_{i}" for i in range(100)]
    values = {k: f"value_of_{v}" if k.startswith("key_") else "error" 
              for v, k in enumerate(data_points)}
    for key, value in values.items():
        matcher.add(key, value)
    test_keys = ["key_0", "nonexistent_key", "key_5"]
    results = []
    for k in test_keys:
        res = matcher.lookup(k)
        results.append((k, res))
    print(results)