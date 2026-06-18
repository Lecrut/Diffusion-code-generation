import threading
from typing import Dict
class NameLookupManager:
    def __init__(self) -> None:
        self._lookup_table: Dict[str, str] = {}
        self._lock = threading.Lock()
    def add_name(self, key: str, value: str) -> bool:
        try:
            with self._lock:
                if not isinstance(key, str):
                    raise TypeError("Key must be a string.")
                if len(value) == 0:
                    raise ValueError("Value cannot be empty.")
                self._lookup_table[key] = value
                return True
        except Exception as exc:
            print(f"Error adding name lookup: {exc}")
            return False
    def get_name(self, key: str) -> str | None:
        try:
            with self._lock:
                if not isinstance(key, str):
                    raise TypeError("Key must be a string.")
                value = self._lookup_table.get(key)
                return value
        except Exception as exc:
            print(f"Error retrieving name lookup: {exc}")
            return None
    def remove_name(self, key: str) -> bool:
        try:
            with self._lock:
                if not isinstance(key, str):
                    raise TypeError("Key must be a string.")
                if key in self._lookup_table:
                    del self._lookup_table[key]
                    return True
                return False
        except Exception as exc:
            print(f"Error removing name lookup: {exc}")
            return False
    def clear(self) -> None:
        with self._lock:
            self._lookup_table.clear()
if __name__ == '__main__':
    manager = NameLookupManager()
    manager.add_name("Alice", "Engineer")
    manager.add_name("Bob", "Designer")
    print(manager.get_name("Alice"))                    
    assert manager.remove_name("Bob") is True
    assert manager.get_name("Bob") is None