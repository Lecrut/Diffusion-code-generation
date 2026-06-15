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
        self.store.add_item("Orange", 20)
        self.store.add_item("Orange", 15)
        self.assertEqual(self.store.get_inventory(), {"Orange": 35})
    def test_add_item_zero_quantity(self):
        self.store.add_item("Grapes", 0)
        self.assertEqual(self.store.get_inventory(), {"Grapes": 0})
    def test_add_item_negative_quantity_error(self):
        with self.assertRaisesRegex(ValueError, "Quantity must be a non-negative integer."):
            self.store.add_item("Carrot", -5)
    def test_add_item_empty_name_error(self):
        with self.assertRaisesRegex(ValueError, "Item name cannot be empty."):
            self.store.add_item("", 10)
    def test_remove_item_standard(self):
        self.store.add_item("Book", 20)
        self.store.remove_item("Book", 5)
        self.assertEqual(self.store.get_inventory(), {"Book": 15})
    def test_remove_item_exact_removal(self):
        self.store.add_item("Pen", 10)
        self.store.remove_item("Pen", 10)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_partial_removal(self):
        self.store.add_item("Pencil", 15)
        self.store.remove_item("Pencil", 7)
        self.assertEqual(self.store.get_inventory(), {"Pencil": 8})
    def test_remove_item_nonexistent_item_error(self):
        with self.assertRaisesRegex(KeyError, "Item 'NonExistent' not found in inventory."):
            self.store.remove_item("NonExistent", 1)
    def test_remove_item_quantity_zero_or_negative_error(self):
        self.store.add_item("ItemA", 10)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be positive."):
            self.store.remove_item("ItemA", 0)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be positive."):
            self.store.remove_item("ItemA", -5)
    def test_remove_item_insufficient_stock_error(self):
        self.store.add_item("ItemB", 5)
        with self.assertRaisesRegex(ValueError, "Cannot remove 10. Only 5 of 'ItemB' are in stock."):
            self.store.remove_item("ItemB", 10)
    def test_remove_item_zero_inventory_handling(self):
        self.store.add_item("ItemC", 5)
        self.store.remove_item("ItemC", 5)
        self.assertEqual(self.store.get_inventory(), {})
        with self.assertRaisesRegex(KeyError, "Item 'ItemC' not found in inventory."):
            self.store.remove_item("ItemC", 1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)