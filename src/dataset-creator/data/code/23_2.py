import threading
class ItemNameManager:
    _instance = None
    _lock = threading.Lock()
    _items = {}
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    def add_item(self, name: str, value: int) -> bool:
        with self._lock:
            if name in self._items:
                current_value = self._items[name]
                new_total = current_value + value
                self._items[name] = max(0, new_total)
                return True
            else:
                self._items[name] = value
                return False
    def get_item(self, name: str) -> int | None:
        with self._lock:
            return self._items.get(name)
if __name__ == '__main__':
    manager1 = ItemNameManager()
    manager2 = ItemNameManager()
    assert manager1 is manager2
    result1 = manager1.add_item("Apple", 50)
    result2 = manager1.add_item("Banana", -10)
    result3 = manager1.get_item("Apple")
    result4 = manager1.get_item("Banana")
    print(f"Is singleton: {manager1 is manager2}")
    print(f"Added Apple (+50): {result1}")
    print(f"Adjusted Banana (-10): {result2}")
    print(f"Apple value: {result3}")
    print(f"Banana value: {result4}")