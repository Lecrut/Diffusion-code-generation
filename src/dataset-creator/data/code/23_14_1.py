from typing import List
class ItemManager:
    def __init__(self) -> None:
        self._items: List[str] = []
    def add_item(self, name: str) -> bool:
        if self._items and name in [item for item in self._items]:
            return False
        self._items.append(name)
        return True
    def get_all_items(self) -> List[str]:
        return self._items.copy()
if __name__ == '__main__':
    manager = ItemManager()
    sample_names = ["Apple", "Banana", "Cherry"]
    for name in sample_names:
        if not manager.add_item(name):
            print(f"Item '{name}' already exists.")
        else:
            print(f"Added item: {name}")
    all_items = manager.get_all_items()
    print("All items:", all_items)