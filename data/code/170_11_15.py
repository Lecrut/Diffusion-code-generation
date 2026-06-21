class Inventory:
    def __init__(self, initial_items=None):
        self.items = initial_items if initial_items else {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity
            if self.items[name] == 0:
                del self.items[name]

    def check_availability(self, name):
        return self.items.get(name, 0)

if __name__ == '__main__':
    my_inventory = Inventory({"Apples": 50, "Bananas": 120, "Oranges": 75})
    print("Initial Inventory:")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")

    my_inventory.add_item("Apples", 30)
    print("\nAdded more Apples:")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")

    my_inventory.remove_item("Bananas", 50)
    print("\nRemoved 50 Bananas:")
    for item, quantity in my_inventory.items.items():
        print(f"{item}: {quantity}")

    print("\nCheck Availability of Oranges:", my_inventory.check_availability("Oranges"))