ITEM_STORAGE_INIT_VALUES = {'apple', 'banana', 'cherry'}

class ItemStore:

    def __init__(self):
        self.items = set(ITEM_STORAGE_INIT_VALUES)

    def add(self, item):
        self.items.add(item)

    def check(self, item):
        return item in self.items
if __name__ == '__main__':
    store = ItemStore()
    print(store.check('apple'))
    print(store.check('orange'))
    store.add('date')
    print(store.check('date'))