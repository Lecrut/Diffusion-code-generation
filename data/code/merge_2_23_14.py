from typing import List
class ItemManager:
    def __init__(self) -> None:
        self._items: dict[str, int] = {}                          
        self._ids_to_names: list[str] = []                                                
    def add_item(self, item_name: str) -> int:
        if item_name in self._items:
            return self._items[item_name]
        new_id = len(self._ids_to_names)
        self._items[item_name] = new_id
        self._ids_to_names.append(item_name)
        return new_id
    def get_item_by_id(self, item_id: int) -> str | None:
        return self._ids_to_names[item_id] if 0 <= item_id < len(self._ids_to_names) else None
    def get_item_by_name(self, item_name: str) -> int | None:
        return self._items.get(item_name)
if __name__ == '__main__':
    manager = ItemManager()
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        "Date",
        "Elderberry"
    ]
    for item in sample_items:
        new_id = manager.add_item(item)
        print(f"Added '{item}' with ID {new_id}")
    target_name = "Banana"
    found_id = manager.get_item_by_name(target_name)
    if found_id is not None:
        original_name = manager.get_item_by_id(found_id)
        print(f"Item '{target_name}' has ID {found_id} and corresponds to '{original_name}'.")
    id_to_get = 2
    name_at_index = manager.get_item_by_id(id_to_get)
    if name_at_index:
        print(f"Item at internal ID {id_to_get} is named '{name_at_index}'.")
    apple_existing_id = manager.add_item("Apple")
    print(f"Re-adding 'Apple' returned existing ID: {apple_existing_id}")