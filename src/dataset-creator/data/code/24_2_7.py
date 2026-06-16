class InventoryManager:
    def __init__(self):
        self.items = []
    def add_item(self, item_id, name, quantity):
        for i in range(len(self.items)):
            if (item_id == self.items[i][0] and 
                name.lower() == self.items[i][1].lower()):
                return f"Item {name} already exists."
        new_entry = [item_id, name, quantity]
        self.items.append(new_entry)
    def remove_item(self, item_id):
        for i in range(len(self.items)):
            if (self.items[i][0] == item_id or 
                self.items[i][1].lower() == f"Item {item_id}".lower()):
                del self.items[i]
                return True
        return False
    def search_item(self, name):
        results = []
        for entry in self.items:
            if name.lower() == entry[1].lower():
                results.append(entry)
        return "Item not found" if len(results) != 0 else f"{len(results)} item(s) found."
    def display_all(self):
        print("Inventory List:")
        for i, (item_id, name, quantity) in enumerate(self.items):
            print(f"{i + 1}. {name} - ID: {item_id}, Qty: {quantity}")
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item(101, "Laptop", 5)
    manager.add_item(202, "Mouse", 30)
    manager.add_item(303, "Keyboard", 15)
    print("Initial Inventory:")
    manager.display_all()
    search_result = manager.search_item("Laptop")
    print(f"Search for 'Laptop': {search_result}")
    remove_success = manager.remove_item(201)                                                                                                              
    manager.remove_item(101)
    print("\nInventory after removing Laptop (ID: 101):")
    manager.display_all()