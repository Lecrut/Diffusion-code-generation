class ItemStore:
    def __init__(self):
        self._items = set()

    def add(self, item):
        self._items.add(item)

    def check(self, item):
        return item in self._items

if __name__ == '__main__':
    store = ItemStore()
    store.add('apple')
    store.add('banana')
    print(store.check('apple'))
    print(store.check('orange'))