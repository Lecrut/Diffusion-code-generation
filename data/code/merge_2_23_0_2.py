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
        except FileNotFoundError:
            self.data[name] = {"id": len(self.data), "status": "active"}
        else:
            if name in self.data:
                return
            new_id = max((item["id"] for item in self.data.values()), default=0) + 1
            self.data[name] = {
                "id": new_id, 
                "status": "active",
                "created_at": None                                                  
            }
    def get_item(self, name: str):
        return self.data.get(name)
def main():
    store = ItemStore()
    sample_items = [
        "Apple", 
        "Banana", 
        "Cherry"
    ]
    for item in sample_items:
        store.add_item(item)
if __name__ == '__main__':
    pass