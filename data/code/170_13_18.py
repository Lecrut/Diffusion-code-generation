class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity):
        if not isinstance(item_id, int) or not isinstance(name, str) or not isinstance(quantity, int):
            raise ValueError("Invalid input types")
        if item_id in self.items:
            raise KeyError(f"Item ID {item_id} already exists")
        self.items[item_id] = {"name": name, "quantity": quantity}

    def remove_item(self, item_id, quantity):
        if not isinstance(item_id, int) or not isinstance(quantity, int):
            raise ValueError("Invalid input types")
        if item_id not in self.items:
            raise KeyError(f"Item ID {item_id} does not exist")
        if self.items[item_id]["quantity"] < quantity:
            raise ValueError(f"Not enough stock for item ID {item_id}")
        self.items[item_id]["quantity"] -= quantity
        if self.items[item_id]["quantity"] == 0:
            del self.items[item_id]

    def query_stock(self, item_id):
        if not isinstance(item_id, int):
            raise ValueError("Invalid input type")
        return self.items.get(item_id, {"name": "Unknown", "quantity": 0})

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(101, "Laptop", 5)
    inventory.add_item(102, "Mouse", 10)
    print(inventory.query_stock(101))
    inventory.remove_item(101, 3)
    print(inventory.query_stock(101))