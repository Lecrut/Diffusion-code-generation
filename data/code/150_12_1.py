class ItemListManager:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item_to_remove):
        try:
            index = self.items.index(item_to_remove)
            self.items.pop(index)
        except ValueError:
            pass
if __name__ == '__main__':
    manager = ItemListManager()
    manager.add_item("apple")
    manager.add_item("banana")
    manager.add_item("apple")
    manager.add_item("orange")
    print("Initial list:", manager.items)
    manager.remove_item("apple")
    print("After removing first 'apple':", manager.items)
    manager.remove_item("grape")
    print("After attempting to remove 'grape' (not found):", manager.items)
    manager.remove_item("banana")
    print("After removing 'banana':", manager.items)