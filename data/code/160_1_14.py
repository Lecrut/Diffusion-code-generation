class ItemStore:
    def __init__(self):
        self.items = set()
    
    def add(self, item):
        self.items.add(item)
    
    def check(self, item):
        return item in self.items

if __name__ == '__main__':
    sample_items = ["orange", "grape", "banana", "kiwi", "apple"]
    store = ItemStore()
    for item in sample_items:
        store.add(item)
    
    print(store.check("apple"))
    print(store.check("cherry"))