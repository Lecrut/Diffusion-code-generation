class ItemManager:
    def __init__(self):
        self.items = ()

    def add_item(self, item_name):
        self.items += (item_name,)

    def search_item(self, query):
        return [item for item in self.items if query.lower() in item.lower()]

    def filter_items(self, predicate):
        return tuple(item for item in self.items if predicate(item))

    def sort_items(self, key=None, reverse=False):
        return tuple(sorted(self.items, key=key, reverse=reverse))

if __name__ == '__main__':
    manager = ItemManager()
    manager.add_item("Apple")
    manager.add_item("Banana")
    manager.add_item("Cherry")
    print(manager.search_item("an"))
    print(manager.filter_items(lambda x: len(x) > 5))
    print(manager.sort_items(key=len, reverse=True))