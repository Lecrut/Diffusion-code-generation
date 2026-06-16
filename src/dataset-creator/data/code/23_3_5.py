class StringItemStore:
    def __init__(self):
        self._items = []
    def add(self, item: str) -> None:
        normalized_item = " ".join(item.lower().split())
        if not any(normalized_item == existing for existing in self._items):
            self._items.append(normalized_item)
    def get_all(self) -> list[str]:
        return [item.upper() for item in self._items]
if __name__ == '__main__':
    store = StringItemStore()
    sample_items = ["hello world", "HELLO WORLD", "  python code  ", "pythoncode"]
    for item in sample_items:
        store.add(item)
    result = store.get_all()
    print(result)