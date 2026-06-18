import json
from pathlib import Path
class ItemStore:
    def __init__(self):
        self.data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        try:
            with open('items.json', 'r') as f:
                data = json.load(f)
            self.data[name] = True
            updated_data = {**data, **self.data}
            Path('items.json').write_text(json.dumps(updated_data))
        except FileNotFoundError:
            Path('items.json').write_text(json.dumps(self.data))
    def get_items(self) -> list[str]:
        return list(self.data.keys())
if __name__ == '__main__':
    store = ItemStore()
    sample_names = ["Apple", "Banana", "Cherry"]
    for name in sample_names:
        store.add_item(name)
    print(store.get_items())