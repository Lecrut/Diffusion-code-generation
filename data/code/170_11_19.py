class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def update_stock(self, name, quantity):
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] < 0:
                self.items[name] = 0
        else:
            raise KeyError(f"Item {name} not found in inventory.")

    def check_availability(self, name):
        return self.items.get(name, 0) > 0

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)

    print("--- Current Inventory ---")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")

    my_inventory.update_stock("Apples", 30)
    print("\n--- Updated Inventory ---")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")

    print("\nAvailability Check:")
    print(f"Apples available: {my_inventory.check_availability('Apples')}")
    print(f"Pears available: {my_inventory.check_availability('Pears')}")