class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return self

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        return self

    def query_item(self, item_name):
        return self.items.get(item_name, 0)

if __name__ == '__main__':
    inventory = Inventory()
    print(f"Initial inventory: {inventory.items}")
    inventory.add_item("apple", 10).add_item("banana", 5)
    print(f"After adding items: {inventory.items}")
    inventory.remove_item("apple", 3)
    print(f"After removing items: {inventory.items}")
    print(f"Query for apple: {inventory.query_item('apple')}")