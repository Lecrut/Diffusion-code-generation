class Inventory:
    INITIAL_ITEMS = {
        "apple": 10,
        "banana": 5,
        "orange": 12
    }

    def __init__(self):
        self.items = dict(Inventory.INITIAL_ITEMS)

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

    def query(self, item_name):
        return self.items.get(item_name, 0)

if __name__ == '__main__':
    inventory = Inventory()
    print(f"Initial inventory: {inventory.items}")
    inventory.add("apple", 5).remove("banana", 1)
    print(f"Updated inventory: {inventory.items}")
    print(f"Quantity of apples: {inventory.query('apple')}")