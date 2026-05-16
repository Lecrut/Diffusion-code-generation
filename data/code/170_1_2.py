class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, details):
        self.items[item_id] = details
    def get_item(self, item_id):
        return self.items.get(item_id)
if __name__ == '__main__':
    inventory = Inventory()
    item1_details = {"name": "Laptop", "quantity": 10, "price": 1200.00}
    inventory.add_item("A001", item1_details)
    item2_details = {"name": "Mouse", "quantity": 50, "price": 25.50}
    inventory.add_item("B002", item2_details)
    print(inventory.get_item("A001"))
    print(inventory.get_item("B002"))
    print(inventory.get_item("C003"))