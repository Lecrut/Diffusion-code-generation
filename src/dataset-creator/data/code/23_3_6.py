import re
class NormalizedStringStore:
    def __init__(self):
        self._items = []
    def add(self, item: str) -> None:
        normalized_item = self.normalize(item)
        if not any(normalized_item == stored for stored in self._items):
            self._items.append(normalized_item)
    @staticmethod
    def normalize(s: str) -> str:
        s = s.lower()
        s = re.sub(r'[^a-z0-9\s]', '', s)
        words = s.split()
        return ' '.join(sorted(words))
if __name__ == '__main__':
    store = NormalizedStringStore()
    store.add("Hello, World!")
    store.add("HELLO WORLD")
    store.add("Python Programming 2024")
    print(f"Stored {len(store._items)} unique normalized items.")