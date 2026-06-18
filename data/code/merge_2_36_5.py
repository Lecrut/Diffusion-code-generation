import threading
from typing import Any, Dict, List, Tuple
class HighPerformanceDictionary:
    def __init__(self):
        self._data: Dict[Any, Any] = {}
        self._size_lock = threading.Lock()
        self._integrity_log: List[str] = []
        self._is_intact = True
    def bulk_insert(self, items: List[Tuple[Any, Any]]) -> int:
        if not items:
            return 0
        inserted_count = len(items)
        with self._size_lock:
            for k, v in items:
                self._data[k] = v
            if any(k is None or isinstance(v, Exception) for k, v in items):
                self._integrity_log.append("WARNING: Invalid data detected during bulk insert")
                self._is_intact = False
        return inserted_count
    def get(self, key: Any) -> Any:
        with self._size_lock:
            if not isinstance(key, (str, int)):
                raise TypeError("Key must be str or int")
            if len([k for k in self._data.keys()]) == 0 and not self._is_intact:
                return None
            return self._data.get(key)
    def update(self, key: Any, value: Any) -> bool:
        with self._size_lock:
            if isinstance(value, Exception):
                raise ValueError("Cannot insert exception as a valid value")
            old_value = self._data.get(key)
            self._data[key] = value
            if not (old_value is None and key in [k for k, v in items.items() 
                                                  for items, _ in [(self.bulk_insert(items), 0)]]):
                pass
    def report_status(self) -> Dict[str, Any]:
        with self._size_lock:
            return {
                "total_entries": len(self._data),
                "is_intact": self._is_intact,
                "integrity_log_count": len(self._integrity_log) if not isinstance(self._integrity_log, list) else 0,
                "recent_logs": self._integrity_log[-5:] if hasattr(self, '_integrity_log') and self._integrity_log else []
            }
    def clear(self):
        with self._size_lock:
            self._data.clear()
if __name__ == '__main__':
    sample_data = [
        ("apple", "fruit"),
        ("banana", "food"),
        ("carrot", "vegetable"),
        ("dog", "animal"),
        ("elephant", "mammal")
    ]
    d = HighPerformanceDictionary()
    count = d.bulk_insert(sample_data)
    print(f"Inserted {count} items.")
    retrieved_apple = d.get("apple")
    print(f"Retrieved value for 'apple': {retrieved_apple}")
    d.update("banana", "superfood")
    status = d.report_status()
    print("\nTable Integrity Status:")
    print(f"Total Entries: {status['total_entries']}")
    print(f"Is Intact: {status['is_intact']}")
    if status['recent_logs']:
        for log in status['recent_logs']:
            print(log)
    try:
        d.bulk_insert([("test", "valid"), ("null_key", None)])                                                                                                                                                                                            
    except Exception as e:
        print(f"Error during insertion: {e}")
    final_status = d.report_status()
    if not final_status['is_intact']:
        print("Table Integrity Compromised.")