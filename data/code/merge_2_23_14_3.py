import json
from typing import List, Dict
class ItemManager:
    def __init__(self) -> None:
        self._items: List[Dict[str, str]] = []
    def add_item(self, name: str, description: str) -> bool:
        existing = next((item for item in self._items if item['name'] == name), None)
        if existing is not None:
            return False
        new_item = {'name': name, 'description': description}
        self._items.append(new_item)
        return True
    def get_all_items(self) -> List[Dict[str, str]]:
        return self._items.copy()
def main():
    manager = ItemManager()
    sample_data = [
        ("Apple", "A round fruit"),
        ("Banana", "A long yellow fruit"),
        ("Carrot", "An orange root vegetable")
    ]
    for name, desc in sample_data:
        if not manager.add_item(name, desc):
            print(f"Item '{name}' already exists.")
        else:
            print(f"Added item: {name}")
    items = manager.get_all_items()
    output_list = []
    for i, item in enumerate(items):
        output_list.append({f"id_{i}": item})
    json_output = json.dumps(output_list)
    print(json_output)
if __name__ == '__main__':
    main()