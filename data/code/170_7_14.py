class Inventory:
    DEFAULT_STOCK = 0

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity + Inventory.DEFAULT_STOCK
        return self

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
        elif item_name in self.items and self.items[item_name] < quantity:
            print(f"Error: Not enough {item_name} in stock")
        else:
            print(f"Error: {item_name} not found in inventory")
        return self

    def query_item(self, item_name):
        return self.items.get(item_name, Inventory.DEFAULT_STOCK)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("apple", 10).add_item("banana", 5)
    print(f"Initial inventory: {inventory.items}")
    inventory.remove_item("apple", 3).remove_item("banana", 2)
    print(f"Updated inventory: {inventory.items}")
    print(f"Remaining apples: {inventory.query_item('apple')}")