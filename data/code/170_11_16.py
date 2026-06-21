INITIAL_QUANTITY = 0

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity + INITIAL_QUANTITY

    def check_availability(self, name, quantity):
        return self.items.get(name, 0) >= quantity

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)

    print("--- Current Inventory ---")
    for item, quantity in inventory.items.items():
        print(f"{item}: {quantity}")

    print("\nAvailability Checks:")
    print(f"Can we sell 30 Apples? {'Yes' if inventory.check_availability('Apples', 30) else 'No'}")
    print(f"Can we sell 150 Bananas? {'Yes' if inventory.check_availability('Bananas', 150) else 'No'}")