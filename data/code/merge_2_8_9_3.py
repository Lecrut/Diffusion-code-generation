import time
class InventoryItem:
    def __init__(self, item_id, name, current_stock, safety_threshold):
        self.item_id = item_id
        self.name = name
        self.current_stock = current_stock
        self.safety_threshold = safety_threshold
        self.reorder_quantity = 0
    def calculate_safety(self):
        return self.safety_threshold
    def needs_reordering(self, sales_velocity_days=7):
        if not isinstance(sales_velocity_days, int) or sales_velocity_days <= 0:
            raise ValueError("Sales velocity days must be a positive integer.")
        daily_sales = (self.current_stock * 1.5 / self.safety_threshold) if self.safety_threshold > 0 else 0
        return self.current_stock < (daily_sales * sales_velocity_days + self.calculate_safety())
    def reorder(self, quantity):
        self.reorder_quantity = quantity
class InventorySystem:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, current_stock, safety_threshold):
        if item_id in self.items:
            raise ValueError(f"Item {item_id} already exists.")
        self.items[item_id] = InventoryItem(item_id, name, current_stock, safety_threshold)
    def check_and_reorder(self, sales_velocity_days=7):
        for item_id, item in self.items.items():
            if item.needs_reordering(sales_velocity_days=sales_velocity_days):
                reorder_qty = int((item.calculate_safety() * 2)) + (int(item.current_stock / 10) * 5)
                item.reorder(reorder_qty)
    def print_status(self, sales_velocity_days=7):
        for item_id in sorted(self.items.keys()):
            item = self.items[item_id]
            status = "NEEDS REORDER" if item.needs_reordering(sales_velocity_days=sales_velocity_days) else "OK"
            reorder_qty = f"[+{item.reorder_quantity}]" if item.reorder_quantity > 0 else ""
            print(f"{status}: {item.name} (Stock: {item.current_stock}) - Reorder Qty:{reorder_qty}")
if __name__ == '__main__':
    system = InventorySystem()
    system.add_item(1, "Laptop", 5, 20)
    system.add_item(2, "Mouse", 30, 8)
    system.add_item(3, "Keyboard", 4, 6)
    print("=== Initial Status ===")
    system.print_status(sales_velocity_days=7)
    time.sleep(1.5)
    print("\n=== After Reorder Check (Simulated Sales Velocity) ===")
    system.check_and_reorder(sales_velocity_days=7)
    system.print_status(sales_velocity_days=7)