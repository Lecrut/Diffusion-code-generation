import time
from typing import Any, Dict, Optional
class OptimizedHashMap:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.load_factor_threshold = 0.75
        self.buckets: list[list[tuple[Any, Any]]] = [[] for _ in range(capacity)]
    def hash_key(self, key: Any) -> int:
        if isinstance(key, str):
            return sum(ord(c) for c in key) % len(self.buckets)
        elif isinstance(key, (int, float)):
            return abs(hash(key)) % len(self.buckets)
        else:
            h = hash(key)
            return abs(h) % len(self.buckets)
    def _rehash_and_resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for key, value in bucket:
                h = self.hash_key(key) % new_capacity
                new_buckets[h].append((key, value))
        self.buckets = new_buckets
    def put(self, key: Any, value: Any) -> None:
        index = self.hash_key(key)
        if len(self.buckets[index]) >= 20 and (len(value) / max(len(self.buckets), 1)) > self.load_factor_threshold:
            self._rehash_and_resize()
        for i, item in enumerate(self.buckets[index]):
            if item[0] == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
    def get(self, key: Any) -> Optional[Any]:
        index = self.hash_key(key)
        for item in self.buckets[index]:
            if item[0] == key:
                return item[1]
        return None
if __name__ == '__main__':
    cache = OptimizedHashMap(capacity=64)
    sample_data = [
        ("user_1", "Alice"),
        ("product_X", "$9.99"),
        ("session_A", 300),
        ("flag_true", True),
        ("item_Y", ["red", "blue"]),
        ("config_v2", {"debug": False}),
    ]
    for key, value in sample_data:
        cache.put(key, value)
    test_queries = [
        ("user_1"),
        ("nonexistent_key"),
        ("product_X"),
        ("session_A")
    ]
    start_time = time.time()
    results = []
    for key in test_queries:
        result = cache.get(key)
        results.append(result)
    end_time = time.time()
    print(f"Lookup Results: {results}")
    print(f"Total Time Taken (ms): {(end_time - start_time) * 1000:.2f}")