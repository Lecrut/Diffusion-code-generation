from typing import List
class ItemManager:
    def __init__(self) -> None:
        self._items: List[str] = []
    def add_item(self, name: str) -> bool:
        if name in self._items:
            return False
        self._items.append(name)
        return True
    def get_all_items(self) -> List[str]:
        return self._items.copy()
    def remove_item(self, name: str) -> bool:
        return self._items.pop(self._items.index(name)) if name in self._items else False
if __name__ == '__main__':
    manager = ItemManager()
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        "Date"
    ]
    for item in sample_items:
        if not manager.add_item(item):
            print(f"{item} already exists.")
    all_items = manager.get_all_items()
    removed = manager.remove_item("Apple")
    final_list = manager.get_all_items()
    if removed:
        print("\nRemoval successful. Final list:")
    else:
        print("\nNo item found for removal.")
    print(final_list)