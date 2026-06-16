import json
from typing import List
class ItemManager:
    def __init__(self):
        self._items: List[str] = []
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings.")
        self._items.append(name)
    def get_all_items(self) -> List[str]:
        return self._items.copy()
    def remove_item(self, name: str) -> bool:
        return self._items.remove(name) if name in self._items else False
def main():
    manager = ItemManager()
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        "Date"
    ]
    for item_name in sample_items:
        manager.add_item(item_name)
    all_items = manager.get_all_items()
    output_data = {
        "total_count": len(all_items),
        "items_list": all_items,
        "sample_removed_check": manager.remove_item("Banana") and not manager.remove_item("Banana")
    }
    print(json.dumps(output_data, indent=2))
if __name__ == '__main__':
    main()