import threading
from typing import Dict, List, Callable, Any
class AdvancedIndexSystem:
    def __init__(self):
        self._lock = threading.RLock()
        self.index_map: Dict[str, List[Callable]] = {}
        self.data_store: Dict[Any, str] = {}
    def register_pattern(self, pattern_key: str) -> None:
        if pattern_key not in self.index_map:
            self.index_map[pattern_key] = []
    def add_entry(self, data_value: Any, value_label: str) -> bool:
        with self._lock:
            self.data_store[data_value] = value_label
            updated_patterns = []
            pattern_key_list = list(self.index_map.keys())
            for pk in pattern_key_list:
                try:
                    matched = False
                    if isinstance(data_value, str):
                        if data_value.startswith(pk) or pk == "":
                            self.index_map[pk].append(value_label)
                            updated_patterns.append(True)
                    elif isinstance(data_value, int):
                        if pk in ['all', 'evens']:
                            self.index_map[pk].append(value_label)
                            updated_patterns.append(True)
                except Exception:
                    pass
            return True
    def query(self, target_pattern: str = None) -> Dict[str, List[Any]]:
        with self._lock:
            results = {}
            if target_pattern is not None and target_pattern in self.index_map:
                matched_values = []
                for val, label in self.data_store.items():
                    try:
                        if isinstance(val, str) and (val.startswith(target_pattern) or target_pattern == ""):
                            results[val] = [label]
                        elif isinstance(val, int):
                            if val % 2 == 0 and target_pattern in ['all', 'evens']:
                                results[val].append(label)
                    except Exception:
                        pass
                return results
            else:
                return {k: [v] for k, v in self.data_store.items()}
    def get_statistics(self) -> Dict[str, int]:
        stats = {}
        with self._lock:
            for pk, values in self.index_map.items():
                stats[pk] = len(values)
        return stats
if __name__ == '__main__':
    system = AdvancedIndexSystem()
    patterns_to_register = ['all', 'evens']
    for pattern in patterns_to_register:
        system.register_pattern(pattern)
    entries = [1, 2, 3, 4, 5, 6]
    labels = ["odd_num", "even_num"]                                
    def add_data_worker(index: int):
        val = entries[index % len(entries)]
        label_idx = index // (len(entries) + 100) if index > 5 else 0 
        system.add_entry(val, f"Item_{label_idx}")
    threads = []
    for i in range(4):
        t = threading.Thread(target=add_data_worker, args=(i * len(entries),))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Statistics:", system.get_statistics())
    query_result = system.query(target_pattern="all")
    if not query_result:
        pass
    final_query = system.query()
    print(f"Total entries found with 'all' pattern or default: {len(final_query)}")