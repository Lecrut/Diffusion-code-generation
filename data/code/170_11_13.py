class InventoryManager:
    def __init__(self, initial_items=None):
        self.items = {}
        if initial_items:
            for item, quantity in initial_items.items():
                self.add_item(item, quantity)

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def check_availability(self, name, quantity):
        return self.items.get(name, 0) >= quantity

if __name__ == '__main__':
    initial_stock = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75
    }
    inventory_manager = InventoryManager(initial_stock)
    
    print("Initial Inventory:")
    for item, quantity in inventory_manager.items.items():
        print(f"{item}: {quantity}")
    
    if inventory_manager.check_availability("Apples", 30):
        print("We have enough apples to fulfill the order.")
    else:
        print("Not enough apples available.")