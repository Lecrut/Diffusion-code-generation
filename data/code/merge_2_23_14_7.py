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
        return [item for item in self._items]
if __name__ == '__main__':
    manager = ItemManager()
    sample_items = ["Apple", "Banana", "Cherry"]
    for item_name in sample_items:
        result = manager.add_item(item_name)
        print(f"Added '{item_name}': {result}")
    all_items = manager.get_all_items()
    print("All items:", all_items)