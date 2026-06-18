import json
class ItemStorage:
    def __init__(self):
        self._data = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._data[name] = True
    def get_items(self) -> list[str]:
        return list(self._data.keys())
if __name__ == '__main__':
    storage = ItemStorage()
    sample_names = ["apple", "banana", "cherry"]
    for name in sample_names:
        storage.add_item(name)
    result_list = storage.get_items()
    output_json = json.dumps(result_list, indent=2)
    print(output_json)