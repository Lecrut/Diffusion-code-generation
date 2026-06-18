class ItemManager:
    def __init__(self, initial_items):
        self.items = initial_items
    def display_items(self):
        for item in self.items:
            print(item)
    def add_item(self, new_item):
        self.items.append(new_item)
if __name__ == '__main__':
    initial_list = ["Apple", "Banana", "Cherry"]
    manager = ItemManager(initial_list)
    print("Initial Item List:")
    manager.display_items()
    manager.add_item("Date")
    print("\nUpdated Item List:")
    manager.display_items()