import threading
class NameLookupManager:
    def __init__(self):
        self._lock = threading.Lock()
        self._data_store = {}
    def add_name(self, key: str, value: str) -> None:
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and value must be strings.")
        try:
            with self._lock:
                self._data_store[key] = value
        except Exception as e:
            raise RuntimeError(f"Failed to add name entry: {e}")
    def get_name(self, key: str) -> str | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        try:
            with self._lock:
                return self._data_store.get(key)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve name entry: {e}")
    def remove_name(self, key: str) -> bool | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        try:
            with self._lock:
                return self._data_store.pop(key, None) is None
        except Exception as e:
            raise RuntimeError(f"Failed to remove name entry: {e}")
if __name__ == '__main__':
    manager = NameLookupManager()
    sample_data = [
        ("alice", "Senior Developer"),
        ("bob", "Product Manager"),
        ("charlie", "Data Scientist")
    ]
    for key, value in sample_data:
        try:
            manager.add_name(key, value)
            print(f"Added {key}: {value}")
        except Exception as error:
            print(f"Error adding data: {error}", file=__import__('sys').stderr)
    test_keys = ["alice", "bob"]
    for key in test_keys:
        try:
            result = manager.get_name(key)
            if result is None:
                raise ValueError(f"No entry found for '{key}'")
            print(f"Retrieved {key}: {result}")
        except Exception as error:
            print(f"Error retrieving data: {error}", file=__import__('sys').stderr)
    manager.remove_name("bob")
    try:
        result = manager.get_name("bob")
        if result is None:
            print("Entry for 'bob' successfully removed.")
        else:
            raise ValueError(f"Expected removal confirmation, got {result}")
    except Exception as error:
        print(f"Error during final check: {error}", file=__import__('sys').stderr)