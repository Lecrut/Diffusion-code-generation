from collections import namedtuple

Item = namedtuple('Item', 'id name quantity price')

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_id, details):
        if item_id in self.items:
            raise ValueError(f'Error: Item {item_id} already exists.')
        self.items[item_id] = details
    
    def get_item(self, item_id):
        return self.items.get(item_id)

if __name__ == '__main__':
    inventory = Inventory()
    try:
        inventory.add_item("A001", {"id": "A001", "name": "Laptop", "quantity": 10, "price": 1200.00})
        inventory.add_item("B002", {"id": "B002", "name": "Mouse", "quantity": 50, "price": 25.50})
        inventory.add_item("C003", {"id": "C003", "name": "Keyboard", "quantity": 30, "price": 75.00})
    except ValueError as e:
        print(e)
    
    item = inventory.get_item("A001")
    if item:
        print(f"Item ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")