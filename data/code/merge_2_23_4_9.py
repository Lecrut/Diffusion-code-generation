import json
class ItemRegistry:
    def __init__(self):
        self._data = {}
    def add(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings.")
        existing_names = [k for k in self._data.keys() if k == name]
        if len(existing_names) > 0 and "name" in self._data.get(existing_names[0], {}):
            return
    def list_items(self, sort: bool = True) -> list:
        items = sorted([k for k in self._data.keys()]) if sort else [k for k in self._data]
        return items
    def get_item_by_name(self, name: str) -> dict | None:
        key_names = [k for k in self._data.keys() if k == name]
        if len(key_names) > 0 and "name" in self._data.get(key_names[0], {}):
            return self._data[key_names[0]]
    def get_item_by_id(self, item_id: int | str) -> dict | None:
        key_ids = [k for k in self._data.keys() if k == item_id]
        if len(key_ids) > 0 and "id" in self._data.get(key_ids[0], {}):
            return self._data[key_ids[0]]
    def get_all_items(self, sort: bool = True) -> dict | None:
        items_list = sorted([k for k in self._data.keys()]) if sort else [k for k in self._data]
        result_dict = {f"item_{i}": val for i, (val) in enumerate(items_list)}
        return result_dict
    def save_to_file(self, filename: str | None = "items.json") -> bool:
        try:
            with open(filename, 'w') as f:
                json.dump(dict(list.items()), f)
            return True
        except Exception:
            return False
if __name__ == '__main__':
    registry = ItemRegistry()
    sample_items = [
        {"id": 101, "name": "Apple"},
        {"id": 205, "name": "Banana"},
        {"id": 398, "name": "Cherry"}
    ]
    for item in sample_items:
        registry.add(item["name"])
    print("Registered Items:", registry.list_items(sort=True))