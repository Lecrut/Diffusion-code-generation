import unittest
class StoreInventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory:
            raise KeyError(f"Item {item_name} not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity to remove must be non-negative")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Cannot remove {quantity}, only {self.inventory[item_name]} of {item_name} available")
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
        with self.assertRaisesRegex(ValueError, "Quantity must be a non-negative integer"):
            self.store.add_item("Grape", -5)
    def test_remove_item_success(self):
        self.store.add_item("Book", 20)
        self.store.remove_item("Book", 5)
        self.assertEqual(self.store.get_inventory(), {"Book": 15})
    def test_remove_item_exact_removal(self):
        self.store.add_item("Pen", 10)
        self.store.remove_item("Pen", 10)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_zero_inventory_error(self):
        self.store.add_item("Eraser", 5)
        self.store.remove_item("Eraser", 5)
        self.assertEqual(self.store.get_inventory(), {})
        with self.assertRaisesRegex(KeyError, "Item Pencil not found in inventory"):
            self.store.remove_item("Pencil", 1)
    def test_remove_item_item_not_found_error(self):
        with self.assertRaisesRegex(KeyError, "Item NonExistent not found in inventory"):
            self.store.remove_item("NonExistent", 1)
    def test_remove_item_insufficient_quantity_error(self):
        self.store.add_item("Candy", 3)
        with self.assertRaisesRegex(ValueError, "Cannot remove 5, only 3 of Candy available"):
            self.store.remove_item("Candy", 5)
    def test_remove_item_negative_quantity_error(self):
        self.store.add_item("Soda", 10)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be non-negative"):
            self.store.remove_item("Soda", -2)
    def test_get_inventory_empty(self):
        self.assertEqual(self.store.get_inventory(), {})
    def test_mixed_operations(self):
        self.store.add_item("ItemA", 100)
        self.store.add_item("ItemB", 50)
        self.store.remove_item("ItemA", 30)
        self.store.add_item("ItemA", 10)
        self.store.remove_item("ItemB", 60)
        expected = {"ItemA": 80}
        self.assertEqual(self.store.get_inventory(), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)