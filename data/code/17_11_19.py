class DynamicCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_final_entry(self):
        if len(self._items) == 0:
            return None
        return self._items[-1]

if __name__ == '__main__':
    collection = DynamicCollection()
    collection.add(10)
    collection.add(20)
    collection.add(30)
    final_entry = collection.get_final_entry()
    print(final_entry)