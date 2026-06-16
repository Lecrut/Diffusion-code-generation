class StringItem:
    def __init__(self, value):
        self._value = str(value).strip().lower()
    @property
    def normalized_value(self) -> str:
        return self._value
    def __str__(self) -> str:
        return f"StringItem({self.normalized_value})"
class StringStorage:
    def __init__(self):
        self._items = []
    def add_item(self, item: StringItem) -> None:
        if not isinstance(item, StringItem):
            raise TypeError("Only StringItem instances can be added.")
        self._items.append(item.normalized_value)
    def get_all_items(self) -> list[str]:
        return [item for item in self._items]
if __name__ == '__main__':
    storage = StringStorage()
    items_data = ["  Hello World! ", "HELLO WORLD", "", None, "123"]
    try:
        valid_items = []
        for data in items_data:
            if isinstance(data, str):
                item = StringItem(data)
                storage.add_item(item)
                valid_items.append(item.normalized_value)
        print(storage.get_all_items())
    except Exception as e:
        pass