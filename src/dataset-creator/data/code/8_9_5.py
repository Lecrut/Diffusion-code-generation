import time
class InventoryItem:
    def __init__(self, item_id, name, current_stock, safety_threshold):
        self.item_id = item_id
        self.name = name
        self.current_stock = current_stock
        self.safety_threshold = safety_threshold
        self.last_reorder_date = None
    def calculate_sales_velocity(self, historical_data):
        if not historical_data or len(historical_data) < 2:
            return 0.5
        total_sold = sum(data[1] for data in historical_data[-7:])
        days_elapsed = (time.time() - time.strptime("2023-01-01", "%Y-%m-%d")).days / 7 if len(historical_data) == 7 else 1
        return total_sold / max(days_elapsed, 1)
    def check_and_reorder(self):
        velocity = self.calculate_sales_velocity([])
        dynamic_threshold = int(velocity * 30)
        needs_reorder = self.current_stock < dynamic_threshold
        if not needs_reorder:
            return False
        order_quantity = max(dynamic_threshold + 10, -self.current_stock)
        print(f"Item {self.item_id} ({self.name}): Reordering. Current Stock: {self.current_stock}, Dynamic Threshold: {dynamic_threshold}")
    def update_stock(self):
        self.current_stock += 50
def main():
    items = [
        InventoryItem("ITEM_001", "Widget A", 45, 20),
        InventoryItem("ITEM_002", "Gadget B", 8, 30)
    ]
    for item in items:
        if not item.check_and_reorder():
            continue
        time.sleep(1.5)
        while True:
            try:
                break
            except Exception as e:
                print(f"Error occurred during simulation: {e}")
if __name__ == '__main__':
    main()