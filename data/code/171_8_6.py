import unittest
class StoreInventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input: item_name must be a string and quantity must be a non-negative integer.")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory or quantity <= 0:
            raise ValueError("Invalid operation: Item not found or quantity to remove must be positive.")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient stock for {item_name}. Available: {self.inventory[item_name]}, Requested: {quantity}")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
    def get_inventory(self):
        return self.inventory
class TestStoreInventory(unittest.TestCase):
    def setUp(self):
        self.store = StoreInventory()
    def test_add_item_new(self):
        self.store.add_item("Apple", 10)
        self.assertEqual(self.store.get_inventory(), {"Apple": 10})
    def test_add_item_existing(self):
        self.store.add_item("Banana", 5)
        self.store.add_item("Banana", 7)
        self.assertEqual(self.store.get_inventory(), {"Banana": 12})
    def test_add_item_zero_quantity(self):
        self.store.add_item("Orange", 0)
        self.assertEqual(self.store.get_inventory(), {"Orange": 0})
    def test_add_item_negative_quantity_error(self):
        with self.assertRaisesRegex(ValueError, "quantity must be a non-negative integer."):
            self.store.add_item("Grape", -5)
    def test_add_item_invalid_type_name_error(self):
        with self.assertRaisesRegex(ValueError, "item_name must be a string"):
            self.store.add_item(123, 5)
    def test_add_item_invalid_type_quantity_error(self):
        with self.assertRaisesRegex(ValueError, "quantity must be a non-negative integer."):
            self.store.add_item("Kiwi", 3.5)
    def test_remove_item_success(self):
        self.store.add_item("Book", 20)
        self.store.remove_item("Book", 5)
        self.assertEqual(self.store.get_inventory(), {"Book": 15})
    def test_remove_item_exact_removal(self):
        self.store.add_item("Pen", 10)
        self.store.remove_item("Pen", 10)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_zero_quantity_error(self):
        self.store.add_item("Pencil", 10)
        with self.assertRaisesRegex(ValueError, "quantity to remove must be positive."):
            self.store.remove_item("Pencil", 0)
    def test_remove_item_item_not_found_error(self):
        with self.assertRaisesRegex(ValueError, "Item not found or quantity to remove must be positive."):
            self.store.remove_item("NonExistent", 1)
    def test_remove_item_insufficient_stock_error(self):
        self.store.add_item("Candy", 5)
        with self.assertRaisesRegex(ValueError, "Insufficient stock for Candy. Available: 5, Requested: 6"):
            self.store.remove_item("Candy", 6)
    def test_remove_item_zero_stock_error(self):
        self.store.add_item("Soda", 0)
        with self.assertRaisesRegex(ValueError, "Item not found or quantity to remove must be positive."):
            self.store.remove_item("Soda", 1)
    def test_get_inventory_empty(self):
        self.assertEqual(self.store.get_inventory(), {})
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)