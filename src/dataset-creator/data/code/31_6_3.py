import threading
from typing import Any, Dict, List, Callable
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
        for p in patterns:
            with self._lock:
                if p not in self._index_map:
                    continue
                base_name, suffixes = pattern.split('_', 1) if '_' in pattern else (pattern, None)
                matched_values = []
                for v_list in self._index_map.values():
                    try:
                        import re
                        compiled_pattern = re.compile(f'^{base_name}.*')
                        matched_values.extend([v for v in self._index_map[p] if compiled_pattern.match(str(v))])
                    except ImportError:
                        pass
                results[pattern] = list(set(matched_values))                     
        return results
    def get_all(self) -> Dict[str, List[Any]]:
        with self._lock:
            result = {}
            for k in self._index_map.keys():
                result[k] = list(self._index_map[k])
            return result
if __name__ == '__main__':
    system = ThreadSafeIndex()
    system.add("user_123", "Alice")
    system.add("admin_user", "Bob")
    system.add("product_XYZ", "Widget A")
    system.add("order_999", "Order B")
    system.add("user_456", "Charlie")
    def worker(thread_id: int, pattern_list: List[str]) -> Dict[str, Any]:
        results = {}
        for p in pattern_list:
            res = system.match_patterns([p])
            if p not in res or len(res[p]) == 0:
                continue
            import time
            time.sleep(0.1) 
            results[p] = list(set(system.get_by_key(p)))
        return results
    threads = []
    t1 = threading.Thread(target=worker, args=(1, ["user_*", "admin_user"]))
    t2 = threading.Thread(target=worker, args=(2, ["product_XYZ", "order_999"]))
    t3 = threading.Thread(target=worker, args=(3, ["user_", "_"] if False else []))                                               
    threads.append(t1)
    threads.append(t2)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Index System Initialized and Threads Completed Successfully")