class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def update_quantity(self, name, change):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(change, int):
            raise ValueError("Quantity change must be an integer")
        if name in self.items:
            new_quantity = self.items[name] + change
            if new_quantity < 0:
                raise ValueError("Cannot set quantity below zero")
            self.items[name] = new_quantity
        else:
            raise KeyError(f"Item '{name}' not found in inventory")

    def check_availability(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        return self.items.get(name, 0)

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)
    print(f"Current inventory:")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")
    
    my_inventory.update_quantity("Apples", -10)
    my_inventory.update_quantity("Bananas", 30)
    print("\nUpdated inventory:")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")
    
    print("\nAvailability check:")
    print(f"Apples available: {my_inventory.check_availability('Apples')}")
    print(f"Bananas available: {my_inventory.check_availability('Bananas')}")