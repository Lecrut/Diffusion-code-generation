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
        return False
    def search_items(self, keyword):
        results = []
        for item_id, data in self.items.items():
            if keyword.lower() in data['name'].lower():
                results.append({'item_id': item_id, 'name': data['name'], 'quantity': data['quantity']})
        return results
    def get_total_quantity(self):
        total = 0
        for data in self.items.values():
            total += data['quantity']
        return total
if __name__ == '__main__':
    inv = InventoryManager()
    inv.add_item('I001', 'Laptop', 5)
    inv.add_item('I002', 'Mouse', 30)
    inv.add_item('I001', 'Laptop', 2)
    print("Total Quantity:", inv.get_total_quantity())
    found = inv.search_items('mouse')
    if found:
        for item in found:
            print(f"Found {item['name']} (ID: {item['item_id']}, Qty: {item['quantity']})")
    removed = inv.remove_item('I002')
    print("Removed I002:", removed)