class Inventory:
    def __init__(self):
        self.items = {}

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
        else:
            raise ValueError(f"Not enough {name} to remove")

    def get_quantity(self, name):
        return self.items.get(name, 0)

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    print(f"Initial inventory: Apples {my_inventory.get_quantity('Apples')}, Bananas {my_inventory.get_quantity('Bananas')}")

    my_inventory.remove_item("Bananas", 30)
    print(f"After removing 30 bananas: Bananas {my_inventory.get_quantity('Bananas')}")

    try:
        my_inventory.remove_item("Grapes", 40)
    except ValueError as e:
        print(e)

    my_inventory.add_item("Oranges", 75)
    my_inventory.add_item("Grapes", 30)
    print(f"Final inventory: Apples {my_inventory.get_quantity('Apples')}, Bananas {my_inventory.get_quantity('Bananas')}, Oranges {my_inventory.get_quantity('Oranges')}, Grapes {my_inventory.get_quantity('Grapes')}")