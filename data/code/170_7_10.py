class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        return self

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return self
        else:
            raise ValueError("Not enough stock or invalid item")

    def get_quantity(self, item_name):
        if not isinstance(item_name, str):
            raise ValueError("Invalid input")
        return self.items.get(item_name, 0)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("apple", 10).add_item("banana", 5)
    print(f"Initial inventory: {inventory.items}")
    try:
        inventory.remove_item("apple", 3).remove_item("banana", 2)
        print(f"Updated inventory: {inventory.items}")
        print(f"Quantity of apple: {inventory.get_quantity('apple')}")
        print(f"Quantity of banana: {inventory.get_quantity('banana')}")
        print(f"Quantity of orange: {inventory.get_quantity('orange')}")
    except ValueError as e:
        print(e)