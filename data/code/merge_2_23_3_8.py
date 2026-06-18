class NormalizedStringStore:
    def __init__(self):
        self._items = []
    def add(self, value: str) -> None:
        normalized_value = " ".join(value.lower().split())
        if not any(item == normalized_value for item in self._items):
            self._items.append(normalized_value)
    def get_count(self) -> int:
        return len(self._items)
    def __repr__(self) -> str:
        return f"NormalizedStringStore({', '.join(repr(i) for i in self._items)})"
if __name__ == '__main__':
    store = NormalizedStringStore()
    sample_data = ["Hello World", "HELLO WORLD!", "hello world.", "WORLD HELLO"]
    for item in sample_data:
        store.add(item)
    print(store)