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
            reorder_amount = max(10, int((self.safety_threshold - self.current_stock) * 2))
            self.reorder_quantity = reorder_amount
            return True
        else:
            self.reorder_quantity = 0
            return False
class InventorySystem:
    def __init__(self):
        self.items = []
    def add_item(self, item_id, name, current_stock, safety_threshold):
        item = InventoryItem(item_id, name, current_stock, safety_threshold)
        self.items.append(item)
    def process_sales_velocity_metric(self, sales_data):
        total_items_sold = sum(sales_data.values())
        if total_items_sold > 0:
            avg_daily_sales = total_items_sold / len(sales_data)
            return max(1.5, avg_daily_sales * 2)
    def check_and_reorder(self):
        for item in self.items:
            sales_velocity = self.process_sales_velocity_metric({item.item_id: 4})
            if item.calculate_reorder(sales_velocity):
                print(f"Reordering {item.name} (ID: {item.item_id}). Quantity to order: {item.reorder_quantity}")
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item("SKU001", "Widget A", 5, 20)
    inventory.add_item("SKU002", "Gadget B", 30, 40)
    inventory.add_item("SKU003", "Tool C", 8, 15)
    print("Inventory Check and Reorder Process Started")
    time.sleep(1)
    inventory.check_and_reorder()