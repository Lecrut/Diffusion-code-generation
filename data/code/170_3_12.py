import threading

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid item name or quantity")
        with self.lock:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid item name or quantity")
        with self.lock:
            if item in self.items and self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                return True
            return False

def print_inventory(inventory):
    print("--- Inventory List ---")
    for item_name, quantity in inventory.items.items():
        print(f"Item: {item_name}, Quantity: {quantity}")
    print("----------------------")

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    try:
        my_inventory.remove_item("Oranges", 75)
    except ValueError as e:
        print(e)
    my_inventory.remove_item("Apples", 30)
    print_inventory(my_inventory)