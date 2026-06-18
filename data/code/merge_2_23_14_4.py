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
    def remove_item(self, name: str) -> bool:
        try:
            self._items.remove(name)
            return True
        except ValueError:
            return False
if __name__ == '__main__':
    manager = ItemManager()
    sample_items = ["Apple", "Banana", "Cherry"]
    for item in sample_items:
        if not manager.add_item(item):
            print(f"Item '{item}' already exists.")
        else:
            print(f"Added item: {item}")
    all_items = manager.get_all_items()
    print("\nAll items:", all_items)
    removed = manager.remove_item("Banana")
    if removed:
        print("Removed 'Banana'.")
    final_list = manager.get_all_items()
    print("Final list of items:", final_list)