class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_final_entry(self):
        if not self._items:
            return None
        return self._items[-1]

if __name__ == '__main__':
    collection = Collection()
    collection.add(10)
    collection.add(20)
    collection.add(30)
    print(collection.get_final_entry())