class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        self.items[name] = self.items.get(name, 0) + quantity

    def check_availability(self, name, quantity):
        return self.items.get(name, 0) >= quantity

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)

    print(f"Available Apples: {my_inventory.check_availability('Apples', 30)}")
    print(f"Available Bananas: {my_inventory.check_availability('Bananas', 150)}")