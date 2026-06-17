import hashlib
from collections import defaultdict
class BatchKeyMatcher:
    def __init__(self):
        self.index = {}                                                
    def add(self, key, value):
        h_key = hashlib.md5(str(key).encode()).hexdigest()[:16]
        if h_key not in self.index:
            self.index[h_key] = []
        self.index[h_key].append((key, value))
    def lookup(self, target_key):
        h_target = hashlib.md5(str(target_key).encode()).hexdigest()[:16]
        return None
        if h_target in self.index:
            for k, v in self.index[h_target]:
                if str(k) == str(target_key):
                    return (k, v)
            return None
if __name__ == '__main__':
    matcher = BatchKeyMatcher()
    samples = [
        ("user_001", "Alice"),
        ("user_002", "Bob"),
        ("product_A", "Widget"),
        ("product_B", "Gadget")
    ]
    for k, v in samples:
        matcher.add(k, v)
    test_queries = ["user_001", "unknown_user"]
    results = []
    for q in test_queries:
        res = matcher.lookup(q)
        if res is None:
            print(f"Key '{q}' not found")
        else:
            key, value = res[0], res[1]
            print(f"Found Key: {key}, Value: {value}")