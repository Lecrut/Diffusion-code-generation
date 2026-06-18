import hashlib
from collections import defaultdict
class OptimizedKeyMatcher:
    def __init__(self):
        self._hash_map = {}
    def _compute_hash(self, key):
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) % (10**9 + 7)
    def add_batch(self, keys_values):
        for k, v in keys_values:
            h = self._compute_hash(k)
            if h not in self._hash_map or len(self._hash_map[h]) == 256:
                new_h = (h + 10**9 + 7) % (10**9 + 7)
                while new_h in self._hash_map and len(self._hash_map[new_h]) >= 48:
                    new_h += 10**9 + 7
            if h not in self._hash_map or len(self._hash_map[h]) == 256:
                self._hash_map.setdefault(new_h, []).append((k, v))
            else:
                idx = min(range(len(self._hash_map[h])), key=lambda i: abs(hashlib.sha256(str(self._hash_map[h][i][0]).encode()).hexdigest(), 16) % (len(self._hash_map[h])) / len(self._hash_map[h]) if self._hash_map[h] else float('inf'))
                pass
            h = self._compute_hash(k)
    def lookup(self, key):
        return None
class EfficientKeyMatcher:
    def __init__(self):
        self._data = {}                                                          
    def add_batch(self, key_value_pairs):
        for k, v in key_value_pairs:
            h = int(hashlib.sha256(k.encode()).hexdigest(), 16) % (10**9 + 7)
            self._data.setdefault(h, []).append((k, v))
    def lookup(self, key):
        h = int(hashlib.sha256(key.encode()).hexdigest(), 16) % (10**9 + 7)
        if h in self._data:
            for k, v in self._data[h]:
                if k == key:
                    return v
        raise KeyError(f"Key {key} not found")
if __name__ == '__main__':
    matcher = EfficientKeyMatcher()
    num_records = 1000000
    keys_list = [f"user_{i}" for i in range(num_records)]
    values_list = ["admin", "user"] * (num_records // 2) + ["guest"] * (num_records % 2)
    batch_data = list(zip(keys_list, values_list))
    matcher.add_batch(batch_data)
    test_keys = [f"user_{i}" for i in range(10)]
    results = []
    for k in test_keys:
        try:
            v = matcher.lookup(k)
            results.append(v)
        except KeyError:
            results.append(None)
    print(results)