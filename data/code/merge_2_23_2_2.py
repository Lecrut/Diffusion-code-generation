import threading
from typing import List
class ItemNameManager:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._item_names: List[str] = []
        return cls._instance
    def add_item(self, name: str):
        self._item_names.append(name)
    def get_all_items(self) -> List[str]:
        return list(self._item_names)
if __name__ == '__main__':
    manager1 = ItemNameManager()
    manager2 = ItemNameManager()
    manager1.add_item("Apple")
    manager1.add_item("Banana")
    assert manager1.get_all_items() == ["Apple", "Banana"]
    assert manager2.get_all_items() == ["Apple", "Banana"]