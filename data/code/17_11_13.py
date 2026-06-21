class OrderedCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_last(self):
        if not self._items:
            raise IndexError("Collection is empty")
        return self._items[-1]

if __name__ == '__main__':
    collection = OrderedCollection()
    collection.add(10)
    collection.add(20)
    collection.add(30)
    print(collection.get_last())