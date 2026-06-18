import hashlib
from collections import defaultdict
class BatchKeyMatcher:
    def __init__(self):
        self.index = {}
    def add(self, key, value):
        if isinstance(key, str) and len(key) > 0:
            hash_key = f"{key}:{hashlib.md5(key.encode()).hexdigest()}"
            self.index[hash_key] = value
    def lookup(self, key):
        return self.index.get(f"{key}:{hashlib.md5(key.encode()).hexdigest()}")
if __name__ == '__main__':
    matcher = BatchKeyMatcher()
    sample_data = [
        ("user_001", "Alice"),
        ("user_002", "Bob"),
        ("product_A", "Widget"),
        ("order_XYZ", "Shipped")
    ]
    for k, v in sample_data:
        matcher.add(k, v)
    test_queries = ["user_001", "unknown_user"]
    results = []
    for q in test_queries:
        res = matcher.lookup(q)
        if res is not None:
            results.append(f"{q}: {res}")
        else:
            results.append(f"{q}: Not Found")
    print("\n".join(results))