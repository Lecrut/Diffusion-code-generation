class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity):
        if not isinstance(item_id, int) or item_id < 1:
            raise ValueError("Item ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.items[item_id] = {"name": name, "quantity": quantity}

    def remove_item(self, item_id, quantity):
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity to remove must be a positive integer")
        if self.items[item_id]["quantity"] < quantity:
            raise ValueError("Not enough stock to remove")
        self.items[item_id]["quantity"] -= quantity
        if self.items[item_id]["quantity"] == 0:
            del self.items[item_id]

    def get_stock_level(self, item_id):
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist")
        return self.items[item_id]["quantity"]

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(101, "Laptop", 5)
    inventory.add_item(102, "Mouse", 10)
    print(inventory.get_stock_level(101))
    inventory.remove_item(101, 2)
    print(inventory.get_stock_level(101))