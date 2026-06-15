class ItemManager:
    def __init__(self, initial_items):
        self.items = list(initial_items)
    def display_items(self):
        for item in self.items:
            print(item)
    def add_item(self, new_item):
        self.items.append(new_item)
if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry"]
    manager = ItemManager(sample_data)
    print("Initial items:")
    manager.display_items()
    manager.add_item("Date")
    print("\nItems after adding a new item:")
    manager.display_items()