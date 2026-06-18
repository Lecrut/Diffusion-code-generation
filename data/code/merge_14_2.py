class ItemStore:
    def __init__(self):
        self.items = {}
    def add_item(self, name):
        self.items[name] = True
if __name__ == '__main__':
    store = ItemStore()
    print("Adding item: Apple")
    store.add_item("Apple")
    print("Adding item: Banana")
    store.add_item("Banana")
    print("Adding item: Apple (duplicate)")
    store.add_item("Apple")
    print("Current items in store:")
    for item in store.items:
        print(item)