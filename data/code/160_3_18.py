class ItemStore:
    def __init__(self):
        self.items = ()
    
    def add_item(self, item_name):
        if item_name not in self.items:
            self.items += (item_name,)
    
    def search_item(self, query):
        return [item for item in self.items if query.lower() in item.lower()]
    
    def filter_items(self, predicate):
        return tuple(item for item in self.items if predicate(item))
    
    def sort_items(self, key=None, reverse=False):
        return tuple(sorted(self.items, key=key, reverse=reverse))

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple")
    store.add_item("Banana")
    store.add_item("Cherry")
    store.add_item("Date")
    print(store.search_item("an"))
    print(store.filter_items(lambda x: len(x) > 5))