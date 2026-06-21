import threading

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()
    
    def add_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid item name or non-positive quantity")
        
        with self.lock:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
    
    def remove_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid item name or non-positive quantity")
        
        with self.lock:
            if item in self.items and self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                return True
            return False
    
    def get_inventory(self):
        with self.lock:
            return dict(self.items)

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Laptop", 1)
    my_inventory.add_item("Mouse", 2)
    print(my_inventory.get_inventory())
    
    success = my_inventory.remove_item("Mouse", 1)
    if success:
        print("Item removed successfully")
    else:
        print("Failed to remove item")
    
    print(my_inventory.get_inventory())