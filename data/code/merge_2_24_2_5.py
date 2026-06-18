class InventoryManager:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, quantity):
        if item_id in self.items:
            current_qty = self.items[item_id]['quantity']
            self.items[item_id] = {'name': name, 'quantity': current_qty + quantity}
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity}
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        return True
    def search_items(self, keyword):
        results = []
        for item_id, data in self.items.items():
            if keyword.lower() in data['name'].lower():
                results.append({'item_id': item_id, 'name': data['name'], 'quantity': data['quantity']})
        return results
if __name__ == '__main__':
    inv = InventoryManager()
    inv.add_item('I001', 'Laptop', 5)
    inv.add_item('I002', 'Mouse', 20)
    inv.add_item('I003', 'Keyboard', 10)
    print("All items:", list(inv.items.values()))
    found = inv.search_items('key')
    if found:
        for item in found:
            print(f"Found {item['name']} (ID: {item['item_id']})")
    inv.remove_item('I002')
    print("After removal:", list(inv.items.values()))