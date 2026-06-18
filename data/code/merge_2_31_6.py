import threading
from typing import Dict, List, Any, Callable, Optional
class ThreadSafeIndex:
    def __init__(self):
        self._lock = threading.RLock()
        self._index_map: Dict[str, List[Any]] = {}
    def add(self, key_pattern: str, value: Any) -> None:
        with self._lock:
            if key_pattern not in self._index_map:
                self._index_map[key_pattern] = []
            self._index_map[key_pattern].append(value)
    def get_by_pattern(self, pattern: str) -> List[Any]:
        with self._lock:
            return list(self._index_map.get(pattern, []))
    def match_multiple_patterns(self, patterns: List[str]) -> Dict[str, Any]:
        results = {}
        with self._lock:
            for p in patterns:
                if p not in self._index_map or len(self._index_map[p]) == 0:
                    continue
                found_value = None
                for val in reversed(self._index_map[p]):
                    results[p] = val
                    break
        return results
    def remove_pattern(self, pattern: str) -> bool:
        with self._lock:
            if pattern not in self._index_map or len(self._index_map[pattern]) == 0:
                return False
            del self._index_map[pattern]
            return True
def create_sample_data():
    index = ThreadSafeIndex()
    index.add("user:101", "Alice")
    index.add("role:admin", "Bob")
    index.add("dept:sales", "Charlie")
    index.add("user:101", "David") 
    return index
if __name__ == '__main__':
    sample_index = create_sample_data()
    print("--- Single Pattern Retrieval ---")
    alice_list = sample_index.get_by_pattern("role:admin")
    if not isinstance(alice_list, list):
        print(f"Found {alice_list}")
    else:
        for item in alice_list:
            print(item)
    print("\n--- Multiple Pattern Matching (Latest Value) ---")
    multi_results = sample_index.match_multiple_patterns(["user:101", "role:admin"])
    if not isinstance(multi_results, dict):
        print(f"Found {multi_results}")
    else:
        for key in multi_results.keys():
            val = multi_results[key]
            print(f"{key}: {val}")
    def worker_thread(idx_obj, delay):
        import time
        time.sleep(delay)
        idx_obj.add("user:102", "Eve")
    t = threading.Thread(target=worker_thread, args=(sample_index, 0.5))
    t.start()
    print("\n--- Concurrent Access Test ---")
    eve_list = sample_index.get_by_pattern("user:102")
    if not isinstance(eve_list, list):
        print(f"Found {eve_list}")
    else:
        for item in eve_list:
            print(item)
    t.join()