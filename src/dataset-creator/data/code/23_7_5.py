import os
from typing import List, Set
class EfficientStorage:
    def __init__(self):
        self._data_store = set()
    def add(self, item: str) -> None:
        if not isinstance(item, str):
            raise TypeError("Only string identifiers are allowed.")
        self._data_store.add(item.lower())
    def contains(self, target: str) -> bool:
        return target.lower() in self._data_store
    def remove(self, item: str) -> None:
        try:
            self._data_store.remove(item.lower())
        except KeyError:
            pass                                                                            
    def get_all(self) -> List[str]:
        return sorted(list(self._data_store))
if __name__ == '__main__':
    storage = EfficientStorage()
    items_to_add = ["ProjectAlpha", "User123", "SystemCore", "DataNode"]
    for item in items_to_add:
        storage.add(item)
    print("Added identifiers:", storage.get_all())
    if storage.contains("user456"):
        print("ID 'USER456' found.")
    else:
        print("ID 'USER456' not found.")
    storage.remove("ProjectAlpha")
    print("After removal:", storage.get_all())