class ItemStore:
    def __init__(self):
        self.items = ()
    
    def add_item(self, item_name):
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Item name must be a non-empty string")
        if item_name in self.items:
            raise ValueError(f"Item '{item_name}' already exists")
        self.items += (item_name,)
    
    def search_item(self, query):
        return tuple(item for item in self.items if query.lower() in item.lower())
    
    def filter_items(self, predicate):
        if not callable(predicate):
            raise TypeError("Predicate must be a callable function")
        return tuple(item for item in self.items if predicate(item))
    
    def sort_items(self, key=None, reverse=False):
        if key is not None and not callable(key):
            raise TypeError("Key must be a callable function or None")
        return tuple(sorted(self.items, key=key, reverse=reverse))

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("Apple")
    store.add_item("Banana")
    store.add_item("Cherry")
    print(store.search_item("an"))
    print(store.filter_items(lambda x: len(x) > 5))
    print(store.sort_items(key=len))
    print(store.sort_items(key=lambda x: x[0], reverse=True))