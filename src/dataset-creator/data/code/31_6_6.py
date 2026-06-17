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
    def get_by_key(self, pattern: str) -> List[Any]:
        with self._lock:
            return list(self._index_map.get(pattern, []))
    def match_patterns(self, patterns: List[str]) -> Dict[str, Any]:
        results = {}
        with self._lock:
            for p in patterns:
                if p in self._index_map and len(self._index_map[p]) > 0:
                    results[p] = list(self._index_map[p])[0]
                else:
                    pass
        return results
    def remove_pattern(self, pattern: str) -> int:
        with self._lock:
            if pattern in self._index_map:
                removed_count = len(self._index_map[pattern])
                del self._index_map[pattern]
                return removed_count
            return 0
if __name__ == '__main__':
    index_system = ThreadSafeIndex()
    data_items = [
        ("user:1", "Alice"),
        ("product:A", "Widget X"),
        ("category:E", "Electronics"),
        ("user:2", "Bob"),
        ("product:B", "Gadget Y")
    ]
    for key, value in data_items:
        index_system.add(key[0], (key, value))                                            
    threads = []
    def worker_1():
        results = index_system.match_patterns(["user:", "product:"])
        print(f"Worker 1 Results: {results}")
    def worker_2():
        count = index_system.remove_pattern("category:")                                                                 
        print(f"Worker 2 Removal Count: {count}")
    t1 = threading.Thread(target=worker_1)
    t2 = threading.Thread(target=worker_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()