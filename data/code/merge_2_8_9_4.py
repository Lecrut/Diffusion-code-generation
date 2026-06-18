import time
class InventoryItem:
    def __init__(self, sku, name, current_stock, safety_threshold):
        self.sku = sku
        self.name = name
        self.current_stock = current_stock
        self.safety_threshold = safety_threshold
        self.reorder_point = 0
    def calculate_reorder_quantity(self):
        return max(1, int((self.safety_threshold - self.current_stock) * 2))
class InventoryManager:
    def __init__(self):
        self.items = {}
    def add_item(self, sku, name, current_stock, safety_threshold):
        if not hasattr(sku, 'calculate_reorder_quantity'):
            item = InventoryItem(sku.name, name, current_stock, safety_threshold)
        else:
            item = sku
        self.items[sku] = item
    def check_and_reorder(self):
        for key in list(self.items.keys()):
            if hasattr(key, 'calculate_reorder_quantity'):
                needed_qty = key.calculate_reorder_quantity()
                current_stock_level = key.current_stock
                if current_stock_level < key.safety_threshold:
                    print(f"Reordering {key.name} (SKU: {key.sku})")
                    new_stock_needed = max(1, int((key.safety_threshold - current_stock_level) * 2))
                    key.reorder_point += new_stock_needed
def main():
    manager = InventoryManager()
    item_a = type('Item', (), {'name': 'Widget A', 'sku': 'W-001'})()
    class MockInventory:
        def __init__(self, name):
            self.name = name
        def calculate_reorder_quantity(self):
            return 5
    manager.add_item("SKU-WA", "Widget Alpha", 2, 10)
    mock_a = type('Mock', (), {'name': 'Alpha Widget'})()
    class MockItem:
        def __init__(self, name, sku, stock):
            self.name = name
            self.sku = sku
            self.current_stock = stock
        def calculate_reorder_quantity(self):
            return 10
    manager.add_item(MockItem("Alpha Widget", "SKU-WA-2", 3))
if __name__ == '__main__':
    pass