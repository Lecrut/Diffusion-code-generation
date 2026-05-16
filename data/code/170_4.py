class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, quantity):
        self.items[item_id] = {"name": name, "quantity": quantity}
    def search_by_id(self, item_id):
        return self.items.get(item_id)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(101, "Laptop", 5)
    inventory.add_item(102, "Mouse", 20)
    inventory.add_item(103, "Keyboard", 15)
    print(inventory.search_by_id(101))
    print(inventory.search_by_id(102))
    print(inventory.search_by_id(999))