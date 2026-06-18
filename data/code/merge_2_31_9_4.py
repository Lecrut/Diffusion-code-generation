import hashlib
from collections import defaultdict
class BatchKeyMatcher:
    def __init__(self):
        self.index = {}
    def add(self, key, value):
        if isinstance(key, str):
            hashed_key = hashlib.sha256(key.encode()).hexdigest()
        else:
            hashed_key = hash(str(key)) % (10**9)
        self.index.setdefault(hashed_key, []).append((key, value))
    def lookup(self, search_key):
        if isinstance(search_key, str):
            hashed_search = hashlib.sha256(search_key.encode()).hexdigest()
        else:
            hashed_search = hash(str(search_key)) % (10**9)
        return self.index.get(hashed_search, [])
def main():
    matcher = BatchKeyMatcher()
    data_points = [
        ("user_001", "Alice"),
        ("user_002", "Bob"),
        ("product_A", "Widget"),
        ("order_XYZ", "Transaction ID 987654321"),
        ("tag_general", "Important Notice")
    ]
    for key, value in data_points:
        matcher.add(key, value)
    test_queries = ["user_001", "product_A", "nonexistent_item"]
    results = []
    for query in test_queries:
        matches = matcher.lookup(query)
        if matches:
            results.append(matches[0][1])
        else:
            results.append(None)
    print(results)
if __name__ == '__main__':
    main()