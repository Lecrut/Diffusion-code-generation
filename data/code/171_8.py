import unittest
class StoreInventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory:
            raise KeyError(f"Item {item_name} not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity to remove must be non-negative.")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Cannot remove {quantity}. Only {self.inventory[item_name]} of {item_name} are in stock.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
    def get_inventory(self):
        return self.inventory
class TestStoreInventory(unittest.TestCase):
    def setUp(self):
        self.store = StoreInventory()
    def test_add_item_new(self):
        self.store.add_item("Apples", 10)
        self.assertEqual(self.store.get_inventory(), {"Apples": 10})
    def test_add_item_existing(self):
        self.store.add_item("Bananas", 5)
        self.store.add_item("Bananas", 7)
        self.assertEqual(self.store.get_inventory(), {"Bananas": 12})
    def test_add_item_zero_quantity(self):
        self.store.add_item("Oranges", 0)
        self.assertEqual(self.store.get_inventory(), {"Oranges": 0})
    def test_add_item_negative_quantity_error(self):
        with self.assertRaisesRegex(ValueError, "Quantity must be a non-negative integer."):
            self.store.add_item("Grapes", -5)
    def test_remove_item_success(self):
        self.store.add_item("Pears", 20)
        self.store.remove_item("Pears", 7)
        self.assertEqual(self.store.get_inventory(), {"Pears": 13})
    def test_remove_item_exact_removal(self):
        self.store.add_item("Carrots", 5)
        self.store.remove_item("Carrots", 5)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_zero_inventory_error(self):
        self.store.add_item("Tomatoes", 0)
        with self.assertRaisesRegex(ValueError, "Cannot remove 1. Only 0 of Tomatoes are in stock."):
            self.store.remove_item("Tomatoes", 1)
    def test_remove_item_insufficient_stock_error(self):
        self.store.add_item("Milk", 5)
        with self.assertRaisesRegex(ValueError, "Cannot remove 6. Only 5 of Milk are in stock."):
            self.store.remove_item("Milk", 6)
    def test_remove_item_nonexistent_item_error(self):
        with self.assertRaisesRegex(KeyError, "Item Cheese not found in inventory."):
            self.store.remove_item("Cheese", 1)
    def test_remove_item_negative_quantity_error(self):
        self.store.add_item("Bread", 10)
        with self.assertRaisesRegex(ValueError, "Quantity to remove must be non-negative."):
            self.store.remove_item("Bread", -2)
    def test_get_inventory_empty(self):
        self.assertEqual(self.store.get_inventory(), {})
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)