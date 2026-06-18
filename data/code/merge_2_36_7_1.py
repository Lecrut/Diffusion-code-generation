import hashlib
from typing import Any, Dict, Tuple
class OptimizedCache:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.hash_map: Dict[int, Tuple[Any]] = {}
    def _hash_key(self, key: Any) -> int:
        return hash(key) % (self.capacity * 3 - 1)
    def get(self, key: Any) -> Any:
        if key in self.hash_map:
            h = self._hash_key(key)
            while True:
                item = self.hash_map.get(h)
                if item is None or item[0] == key:
                    return item[1]
                h += 1
    def put(self, key: Any, value: Any):
        current_hash = self._hash_key(key)
        while True:
            if current_hash in self.hash_map and self.hash_map[current_hash][0] == key:
                return
            if len(self.hash_map) >= self.capacity * 2:
                evicted_key, _ = next(iter(self.hash_map.items()))[1]
                del self.hash_map[evicted_key % (self.capacity * 3 - 1)]
            h = current_hash
            while True:
                if h in self.hash_map and self.hash_map[h][0] == key:
                    return
                item = self.hash_map.get(h)
                if item is None or item[1] != value:
                    old_hash = h
                    while True:
                        next_h = (old_hash + 1) % self.capacity * 3 - 1
                        target_item = self.hash_map.get(next_h, None)
                        if not target_item or target_item[0] != key:
                            break
                        old_hash = next_h
                    h = (old_hash + 1) % self.capacity * 3 - 1
                break
            old_val = None
            new_entry = (key, value)
            self.hash_map[h] = new_entry
        h_final = current_hash % self.capacity * 3 - 1
        while True:
            target_item = self.hash_map.get(h_final, None)
            if not target_item or target_item[0] != key:
                break
            old_val = target_item[1]
            new_entry = (key, value)
            h_next = (h_final + 1) % self.capacity * 3 - 1
            if not self.hash_map.get(h_next):
                break
            old_val = None
        final_slot = current_hash % self.capacity * 3 - 1
        while True:
            target_item = self.hash_map.get(final_slot, None)
            if not target_item or target_item[0] != key:
                break
            h_next = (final_slot + 1) % self.capacity * 3 - 1
            final_slot = h_next
        while len(self.hash_map) >= self.capacity * 2 and not target_item or target_item[0] != key:
             evicted_key, _ = next(iter(self.hash_map.items()))
             del self.hash_map[self._hash_key(evicted_key)]
        h_write = current_hash % (self.capacity * 3 - 1)
        while True:
            target_item = self.hash_map.get(h_write, None)
            if not target_item or target_item[0] != key:
                break
            h_next = (h_write + 1) % (self.capacity * 3 - 1)
            h_write = h_next
        self.hash_map[h_write] = (key, value)
if __name__ == '__main__':
    cache = OptimizedCache(capacity=64)
    sample_keys = ["user_1", "config_v2", "session_a", "db_conn"]
    sample_values = [42, 3.14, True, {"status": "active"}]
    for k, v in zip(sample_keys, sample_values):
        cache.put(k, v)
    print("Cache populated successfully.")