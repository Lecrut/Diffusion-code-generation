class OrderedCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_last(self):
        if not self._items:
            return None
        return self._items[-1]

if __name__ == '__main__':
    collection = OrderedCollection()
    collection.add(1)
    collection.add(2)
    collection.add(3)
    print(collection.get_last())