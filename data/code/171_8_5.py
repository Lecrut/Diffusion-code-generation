import unittest
class StoreInventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if item_name == "":
            raise ValueError("Item name cannot be empty.")
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if quantity <= 0:
            raise ValueError("Quantity to remove must be positive.")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Cannot remove {quantity}. Only {self.inventory[item_name]} of '{item_name}' are in stock.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
    def get_inventory(self):
        return self.inventory
class TestStoreInventory(unittest.TestCase):
    def setUp(self):
        self.store = StoreInventory()
    def test_add_item_standard(self):
        self.store.add_item("Apple", 10)
        self.assertEqual(self.store.get_inventory(), {"Apple": 10})
        self.store.add_item("Banana", 5)
        self.assertEqual(self.store.get_inventory(), {"Apple": 10, "Banana": 5})
    def test_add_item_multiple_additions(self):
        self.store.add_item("Book", 20)
        self.store.add_item("Book", 5)
        self.assertEqual(self.store.get_inventory(), {"Book": 25})
    def test_add_item_zero_quantity(self):
        self.store.add_item("Orange", 0)
        self.assertEqual(self.store.get_inventory(), {"Orange": 0})                                                                                                                                                                                                                                                
        self.assertEqual(self.store.get_inventory(), {"Orange": 0})
    def test_add_item_negative_quantity_error(self):
        with self.assertRaisesRegex(ValueError, "Quantity must be a non-negative integer."):
            self.store.add_item("Grape", -5)
    def test_add_item_empty_name_error(self):
        with self.assertRaisesRegex(ValueError, "Item name cannot be empty."):
            self.store.add_item("", 10)
    def test_remove_item_standard(self):
        self.store.add_item("Pen", 20)
        self.store.remove_item("Pen", 5)
        self.assertEqual(self.store.get_inventory(), {"Pen": 15})
    def test_remove_item_exact_removal(self):
        self.store.add_item("Eraser", 10)
        self.store.remove_item("Eraser", 10)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_partial_removal(self):
        self.store.add_item("Pencil", 30)
        self.store.remove_item("Pencil", 7)
        self.assertEqual(self.store.get_inventory(), {"Pencil": 23})
    def test_remove_item_nonexistent_item_error(self):
        with self.assertRaisesRegex(KeyError, "Item 'Marker' not found in inventory."):
            self.store.remove_item("Marker", 1)
    def test_remove_item_quantity_error_zero(self):
        self.store.add_item("Ruler", 5)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be positive."):
            self.store.remove_item("Ruler", 0)
    def test_remove_item_quantity_error_negative(self):
        self.store.add_item("Ruler", 5)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be positive."):
            self.store.remove_item("Ruler", -2)
    def test_remove_item_insufficient_stock_error(self):
        self.store.add_item("Stapler", 5)
        with self.assertRaisesRegex(ValueError, "Cannot remove 6. Only 5 of 'Stapler' are in stock."):
            self.store.remove_item("Stapler", 6)
    def test_remove_item_zero_inventory_handling(self):
        self.store.add_item("EmptyBox", 0)
        self.assertEqual(self.store.get_inventory(), {"EmptyBox": 0})
        with self.assertRaisesRegex(KeyError, "Item 'EmptyBox' not found in inventory."):
            self.store.remove_item("EmptyBox", 1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)