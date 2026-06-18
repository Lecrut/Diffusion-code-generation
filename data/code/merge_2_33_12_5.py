import threading
class NameLookupManager:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def add_name(self, key: str, value: str) -> None:
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and Value must be strings.")
        with self._lock:
            self._data[key] = value
    def get_name(self, key: str) -> str | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        with self._lock:
            return self._data.get(key)
    def remove_name(self, key: str) -> bool | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        with self._lock:
            return self._data.pop(key, None)
    def contains(self, key: str) -> bool | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        with self._lock:
            return key in self._data
if __name__ == '__main__':
    manager = NameLookupManager()
    sample_data = {
        "john_doe": "Engineer",
        "jane_smith": "Designer",
        "bob_jones": "Analyst"
    }
    for k, v in sample_data.items():
        manager.add_name(k, v)
    assert manager.contains("john_doe") is True
    assert manager.get_name("jane_smith") == "Designer"
    removed = manager.remove_name("bob_jones")
    assert removed == "Analyst"
    assert not manager.contains("bob_jones")
    print(f"All tests passed. Sample lookup result: {manager.get_name('john_doe')}")