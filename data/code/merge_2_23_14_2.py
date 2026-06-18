from typing import List
class ItemManager:
    def __init__(self) -> None:
        self._items: List[str] = []
    def add_item(self, name: str) -> bool:
        if name in self._items:
            return False
        self._items.append(name)
        return True
    def remove_item(self, name: str) -> bool:
        return self._items.pop(self._items.index(name)) == name
    def get_all_items(self) -> List[str]:
        return self._items.copy()
if __name__ == '__main__':
    manager = ItemManager()
    sample_items = ["Apple", "Banana", "Cherry"]
    for item in sample_items:
        if not manager.add_item(item):
            print(f"Item '{item}' already exists.")
        else:
            print(f"Added {item}.")
    all_items = manager.get_all_items()
    print("Current inventory:", all_items)