class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def check_availability(self, name, required_quantity):
        return self.items.get(name, 0) >= required_quantity

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)

    print(f"Apples in stock: {inventory.check_availability('Apples', 30)}")
    print(f"Bananas in stock: {inventory.check_availability('Bananas', 150)}")