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
    @property
    def count(self) -> int:
        return len(self._items)
if __name__ == '__main__':
    storage = StringStorage()
    sample_items = [
        "  Hello World! ",
        "HELLO WORLD",
        "",
        None,
        12345
    ]
    for raw in sample_items:
        try:
            item = StringItem(raw) if raw is not None else StringItem("")
            storage.add_item(item)
        except Exception as e:
            print(f"Error processing '{raw}': {e}")
    print(storage.count)