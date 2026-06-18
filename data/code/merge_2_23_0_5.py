import json
from pathlib import Path
class ItemStore:
    def __init__(self):
        self.data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Item name must be a non-empty string.")
        self.data[name] = True
    def get_items(self) -> list[str]:
        return list(self.data.keys())
    def remove_item(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False
def load_from_file(filepath: Path) -> ItemStore:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        store = ItemStore()
        for name in data.get('items', []):
            if isinstance(name, str):
                store.add_item(name.strip())
        return store
    except (FileNotFoundError, json.JSONDecodeError):
        return ItemStore()
def save_to_file(store: ItemStore, filepath: Path) -> None:
    items = [item for item in store.get_items()]
    data = {'items': items}
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    store = ItemStore()
    for item in sample_data:
        try:
            store.add_item(item)
        except ValueError as e:
            print(f"Error adding {item}: {e}")
    save_to_file(store, Path('items.json'))
    retrieved_items = store.get_items()
    if len(retrieved_items) > 0:
        print("Stored items:", ', '.join(retrieved_items))