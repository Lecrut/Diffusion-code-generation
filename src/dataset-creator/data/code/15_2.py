class InventoryManager:
    def __init__(self, item_names):
        self.items = item_names
    def display_inventory(self):
        for item in self.items:
            print(item)
if __name__ == '__main__':
    initial_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    manager = InventoryManager(initial_items)
    manager.display_inventory()