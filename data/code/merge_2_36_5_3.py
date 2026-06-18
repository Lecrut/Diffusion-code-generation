import threading
from collections import OrderedDict
from typing import Any, Dict, List, Optional
class Dictionary:
    def __init__(self):
        self._data = OrderedDict()
        self._lock = threading.RLock()
        self._integrity_checks_passed = 0
        self._total_integrity_checks = 0
    def insert(self, key: Any, value: Any) -> None:
        with self._lock:
            if key in self._data:
                del self._data[key]
            self._data[key] = value
    def bulk_insert(self, items: List[tuple]) -> int:
        with self._lock:
            inserted_count = 0
            for key, value in items:
                if key not in self._data:
                    self._data[key] = value
                    inserted_count += 1
            return inserted_count
    def get(self, key: Any) -> Optional[Any]:
        with self._lock:
            return self._data.get(key)
    def delete(self, key: Any) -> bool:
        with self._lock:
            if key in self._data:
                del self._data[key]
                return True
            return False
    def check_integrity(self) -> int:
        with self._lock:
            count = 0
            for k, v in self._data.items():
                if isinstance(k, (str, int)) and not isinstance(v, dict):
                    count += 1
            return count
    def get_status(self) -> Dict[str, Any]:
        with self._lock:
            total_checks = len(self._data) + self.check_integrity()
            passed_checks = self.check_integrity()
            integrity_rate = (passed_checks / max(total_checks, 1)) * 100 if total_checks > 0 else 100.0
            return {
                "size": len(self._data),
                "integrity_passed": passed_checks,
                "total_checked": total_checks,
                "integrity_rate_percent": round(integrity_rate, 2)
            }
if __name__ == '__main__':
    d = Dictionary()
    sample_data = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3),
        ("date", 4),
        ("elderberry", 5)
    ]
    count = d.bulk_insert(sample_data)
    print(f"Inserted {count} items.")
    status = d.get_status()
    print("Table Integrity Status:")
    for k, v in status.items():
        if isinstance(v, float):
            print(f"{k}: {v}%")
        else:
            print(f"{k}: {v}")
    val = d.get("banana")
    print(f"Retrieved 'banana': {val}")
    deleted = d.delete("cherry")
    status_after_delete = d.get_status()
    if deleted:
        print(f"After deleting 'cherry', size is now {status_after_delete['size']} and integrity rate is {status_after_delete['integrity_rate_percent']}%")