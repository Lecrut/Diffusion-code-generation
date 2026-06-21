class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return self

    def remove(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        return self

    def get_quantity(self, item_name):
        return self.items.get(item_name, 0)

if __name__ == '__main__':
    inventory = Inventory()
    print(f"Initial inventory: {inventory.items}")
    inventory.add("apple", 10).add("banana", 5).add("orange", 12)
    print(f"After adding items: {inventory.items}")
    inventory.remove("apple", 3).remove("banana", 1)
    print(f"After removing items: {inventory.items}")
    print(f"Quantity of apple: {inventory.get_quantity('apple')}")