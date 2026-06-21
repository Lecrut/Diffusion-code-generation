class ItemStore:

    def __init__(self):
        self.items = set()

    def add(self, item):
        if item not in self.items:
            self.items.add(item)

    def check(self, item):
        return item in self.items
if __name__ == '__main__':
    store = ItemStore()
    store.add('apple')
    store.add('banana')
    print(store.check('apple'))
    print(store.check('orange'))