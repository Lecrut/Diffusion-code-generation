class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return self

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError("Insufficient inventory")
        return self

    def get_quantity(self, item_name):
        if not isinstance(item_name, str):
            raise ValueError("Invalid input")
        return self.items.get(item_name, 0)

if __name__ == '__main__':
    inventory = Inventory()
    print(f"Initial inventory: {inventory.items}")
    try:
        inventory.add_item("apple", 15).add_item("banana", 7)
        print(f"After adding items: {inventory.items}")
        inventory.remove_item("apple", 5)
        print(f"After removing 5 apples: {inventory.items}")
        print(f"Quantity of bananas: {inventory.get_quantity('banana')}")
    except ValueError as e:
        print(e)