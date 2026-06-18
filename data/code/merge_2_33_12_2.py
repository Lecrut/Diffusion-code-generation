import threading
class NameLookupManager:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()
    def add(self, key: str, value: str) -> None:
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and value must be strings.")
        with self._lock:
            self._data[key] = value
    def get(self, key: str) -> str | None:
        with self._lock:
            return self._data.get(key)
    def remove(self, key: str) -> bool:
        with self._lock:
            return self._data.pop(key, None) is not None
if __name__ == '__main__':
    manager = NameLookupManager()
    manager.add("alice", "Alice Smith")
    manager.add("bob", "Robert Jones")
    print(manager.get("alice"))                       
    print(manager.remove("bob"))                
    print(manager.get("bob"))