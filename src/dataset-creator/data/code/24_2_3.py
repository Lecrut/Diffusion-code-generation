class InventoryManager:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, quantity):
        if item_id in self.items:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self.items[item_id] = {"name": name, "quantity": quantity}
    def remove_item(self, item_id):
        if item_id not in self.items:
            return False
        del self.items[item_id]
        return True
    def search_items(self, keyword):
        results = []
        for item_id, data in self.items.items():
            if keyword.lower() in data["name"].lower():
                results.append({"item_id": item_id, "data": data})
        return results
if __name__ == '__main__':
    inv = InventoryManager()
    inv.add_item("I001", "Laptop", 5)
    inv.add_item("I002", "Mouse", 30)
    inv.add_item("I003", "Keyboard", 15)
    inv.add_item("I004", "Monitor", 8)
    print("Search for 'Laptop':")
    results = inv.search_items("laptop")
    if not results:
        print("No matches found.")
    else:
        for res in results:
            print(f"ID: {res['item_id']}, Name: {res['data']['name']}, Qty: {res['data']['quantity']}")
    inv.remove_item("I002")
    print("\nRemoved I002.")
    print("\nSearch for 'Mouse':")
    results = inv.search_items("mouse")
    if not results:
        print("No matches found.")
    else:
        for res in results:
            print(f"ID: {res['item_id']}, Name: {res['data']['name']}, Qty: {res['data']['quantity']}")
    print("\nTotal items remaining:", len(inv.items))