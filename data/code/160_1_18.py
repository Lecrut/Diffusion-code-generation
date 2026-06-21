class ItemStore:
    def __init__(self):
        self.items = set()
    
    def add(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        self.items.add(item)
    
    def check(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        return item in self.items

if __name__ == '__main__':
    store = ItemStore()
    store.add('apple')
    store.add('banana')
    print(store.check('apple'))
    print(store.check('orange'))