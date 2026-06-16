import re
class StringItemStore:
    def __init__(self):
        self._items = []
    def add(self, item: str) -> None:
        normalized_item = self.normalize(item)
        if not any(normalized_item == existing for existing in self._items):
            self._items.append(normalized_item)
    @staticmethod
    def normalize(s: str) -> str:
        s = s.strip().lower()
        s = re.sub(r'\s+', ' ', s)
        return s
if __name__ == '__main__':
    store = StringItemStore()
    sample_items = ["  Hello World! ", "HELLO WORLD", "hello world"]
    for item in sample_items:
        store.add(item)
    print(store._items)