import threading
from typing import Dict
class NameLookupManager:
    def __init__(self) -> None:
        self._lookup_table: Dict[str, str] = {}
        self._lock = threading.Lock()
    def add_name(self, key: str, value: str) -> bool:
        with self._lock:
            if key in self._lookup_table:
                return False
            try:
                self._lookup_table[key] = value
                return True
            except Exception as e:
                raise RuntimeError(f"Failed to add name '{key}': {e}")
    def get_name(self, key: str) -> str | None:
        with self._lock:
            try:
                return self._lookup_table.get(key)
            except Exception as e:
                raise RuntimeError(f"Failed to retrieve name '{key}': {e}")
    def remove_name(self, key: str) -> bool:
        with self._lock:
            try:
                if key in self._lookup_table:
                    del self._lookup_table[key]
                    return True
                return False
            except Exception as e:
                raise RuntimeError(f"Failed to remove name '{key}': {e}")
    def clear(self) -> None:
        with self._lock:
            try:
                self._lookup_table.clear()
            except Exception as e:
                raise RuntimeError("Failed to clear lookup table:") from e
if __name__ == '__main__':
    manager = NameLookupManager()
    sample_data = [
        ("alice", "Alice Smith"),
        ("bob", "Bob Jones"),
        ("charlie", "Charlie Brown")
    ]
    for key, value in sample_data:
        if not manager.add_name(key, value):
            print(f"Warning: Duplicate entry attempted for '{key}'")
    try:
        result = manager.get_name("alice")
        assert isinstance(result, str), "Result should be a string."
        print(f"Retrieved name for 'alice': {result}")
    except Exception as e:
        raise RuntimeError(f"Lookup failed unexpectedly: {e}") from e
    try:
        result = manager.get_name("unknown_user")
        assert isinstance(result, type(None)), "Result should be None."
        print(f"Retrieved name for 'unknown_user': {result}")
    except Exception as e:
        raise RuntimeError(f"Lookup failed unexpectedly: {e}") from e
    try:
        manager.remove_name("alice")
        assert not manager.get_name("alice"), "Name should be removed."
        print("Successfully removed name for 'alice'")
    except Exception as e:
        raise RuntimeError(f"Removal failed unexpectedly: {e}") from e