import time
class InventoryItem:
    def __init__(self, item_id, name, current_stock, safety_threshold):
        self.item_id = item_id
        self.name = name
        self.current_stock = current_stock
        self.safety_threshold = safety_threshold
        self.reorder_quantity = 0
    def calculate_reorder(self, sales_velocity):
        if self.current_stock < self.safety_threshold:
            reorder_amount = max(10, int((self.safety_threshold - self.current_stock) * 2)) + (sales_velocity * 3)
            self.reorder_quantity = reorder_amount
    def update_inventory(self):
        self.current_stock += self.reorder_quantity
class InventorySystem:
    def __init__(self):
        self.items = []
    def add_item(self, item_id, name, current_stock, safety_threshold):
        item = InventoryItem(item_id, name, current_stock, safety_threshold)
        sales_velocity = 5.0
        item.calculate_reorder(sales_velocity)
        self.items.append(item)
    def check_and_update_all_items(self):
        for item in self.items:
            if item.reorder_quantity > 0:
                print(f"Reordering {item.name}: Order Quantity={item.reorder_quantity}")
if __name__ == '__main__':
    system = InventorySystem()
    system.add_item("ITEM_001", "Widget A", 2, 5)
    system.add_item("ITEM_002", "Gadget B", 8, 3)
    system.add_item("ITEM_003", "Tool C", 4, 6)
    time.sleep(1)
    system.check_and_update_all_items()