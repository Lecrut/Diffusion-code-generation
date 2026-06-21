import threading

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        with self.lock:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_item(self, item, quantity):
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
    sample_items = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75,
        "Grapes": 30
    }
    my_inventory = Inventory()
    for item, quantity in sample_items.items():
        my_inventory.add_item(item, quantity)
    print_inventory(my_inventory)