ITEM_NAMES = {"apple", "banana", "cherry", "date", "elderberry"}

class ItemStore:
    def __init__(self):
        self.items = set(ITEM_NAMES)
    
    def add(self, item):
        self.items.add(item)
    
    def check(self, item):
        return item in self.items

if __name__ == '__main__':
    store = ItemStore()
    print(store.check('apple'))
    print(store.check('orange'))