class ItemStore:

    def __init__(self, initial_items=None):
        if not isinstance(initial_items, (type(None), list, set)):
            raise ValueError('Initial items must be None, a list, or a set')
        self.items = set() if initial_items is None else set(initial_items)

    def add(self, item):
        if not isinstance(item, str):
            raise ValueError('Item must be a string')
        self.items.add(item)

    def check(self, item):
        return item in self.items
if __name__ == '__main__':
    store = ItemStore(['apple', 'banana'])
    store.add('cherry')
    print(store.check('apple'))
    print(store.check('orange'))