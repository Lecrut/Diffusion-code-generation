class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity):
        if not isinstance(name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
    
    def remove_item(self, name, quantity):
        if not isinstance(name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input")
        if name not in self.items or self.items[name] < quantity:
            raise KeyError("Item not found or insufficient quantity")
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]
    
    def display_inventory(self):
        print("--- Inventory ---")
        if not self.items:
            print("Inventory is empty.")
            return
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
        print("-----------------")

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.remove_item("Apples", 20)
    my_inventory.display_inventory()