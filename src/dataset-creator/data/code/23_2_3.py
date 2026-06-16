import threading
from typing import List
class ItemNameManager:
    _instance = None
    _lock = threading.Lock()
    _items: List[str] = []
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._items = []
        return cls._instance
    def add_item(self, name: str) -> bool:
        with self._lock:
            if name not in self._items:
                self._items.append(name)
                return True
            return False
    def remove_item(self, name: str) -> bool:
        with self._lock:
            if name in self._items:
                self._items.remove(name)
                return True
            return False
    def get_all_items(self) -> List[str]:
        with self._lock:
            return list(self._items)
if __name__ == '__main__':
    manager = ItemNameManager()
    manager.add_item("Widget")
    manager.add_item("Gadget")
    print(manager.get_all_items())