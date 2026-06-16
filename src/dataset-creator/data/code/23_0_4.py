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
            Path('items.json').write_text(json.dumps(updated_data), encoding='utf-8')
        except FileNotFoundError:
            with open('items.json', 'w') as f:
                json.dump(self.data, f)
    def get_items(self) -> list[str]:
        try:
            with open('items.json', 'r') as f:
                data = json.load(f)
            return sorted(data.keys())
        except FileNotFoundError:
            return []
if __name__ == '__main__':
    store = ItemStore()
    sample_items = [
        "apple",
        "banana",
        "cherry"
    ]
    for item in sample_items:
        store.add_item(item)
    retrieved_items = store.get_items()
    print(retrieved_items)