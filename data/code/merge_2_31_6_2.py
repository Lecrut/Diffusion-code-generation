import threading
from typing import Any, Dict, List, Callable
class ThreadSafeIndex:
    def __init__(self):
        self._lock = threading.RLock()
        self._index_map: Dict[str, List[Callable]] = {}                                      
        self._value_store: Dict[Any, str] = {}                                  
    def register_pattern(self, pattern: str):
        with self._lock:
            if pattern not in self._index_map:
                self._index_map[pattern] = []
    def index_value(self, data: Any, primary_key: str) -> bool:
        with self._lock:
            matches_found = False
            current_patterns_for_value = []
            for p, callbacks in list(self._index_map.items()):
                if callable(callbacks):                                                             
                    try:
                        result = data == callback(p)
                        matches_found |= result
                        self.value_store[data] = p
                    except Exception:
                        pass
            return matches_found
    def query_by_pattern(self, pattern: str, target_value: Any) -> List[Any]:
        with self._lock:
            results = []
            if pattern in self.value_store:
                for val in self.value_store.values():
                    try:
                        match_result = target_value == eval(val)                                       
                        if match_result:
                            results.append(val)
                    except Exception:
                        pass
            return results
    def get_indexed_values(self, pattern: str) -> List[Any]:
        with self._lock:
            matches = []
            for val in self.value_store.values():
                try:
                    key_val = eval(val)                                                  
                    if target_value == pattern or (isinstance(key_val, str) and key_val.startswith(pattern)):
                        matches.append(val)
                except Exception:
                    pass
            return matches
if __name__ == '__main__':
    index_system = ThreadSafeIndex()
    data_points = [100, "active", 2.5, True]
    def is_numeric(pattern): return isinstance(data[0], int or float) and pattern == 'numeric'
    index_system.register_pattern('numeric')
    index_system.index_value(100, "key_1")                                  
    thread = threading.Thread(target=lambda: print(f"Thread result for numeric query: {index_system.query_by_pattern('numeric', 2.5)}"))
    thread.start()