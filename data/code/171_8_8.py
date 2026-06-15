import unittest
class StoreInventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input for add_item")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory:
            raise ValueError(f"Item {item_name} not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity to remove cannot be negative")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient stock for {item_name}")
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
    def test_add_item_invalid_input(self):
        with self.assertRaisesRegex(ValueError, "Invalid input for add_item"):
            self.store.add_item(123, 5)
        with self.assertRaisesRegex(ValueError, "Invalid input for add_item"):
            self.store.add_item("Pen", -5)
    def test_remove_item_success(self):
        self.store.add_item("Book", 20)
        self.store.remove_item("Book", 5)
        self.assertEqual(self.store.get_inventory(), {"Book": 15})
    def test_remove_item_to_zero(self):
        self.store.add_item("Pen", 3)
        self.store.remove_item("Pen", 3)
        self.assertEqual(self.store.get_inventory(), {})
    def test_remove_item_insufficient_stock(self):
        self.store.add_item("Soda", 10)
        with self.assertRaisesRegex(ValueError, "Insufficient stock for Soda"):
            self.store.remove_item("Soda", 11)
    def test_remove_item_not_found(self):
        with self.assertRaisesRegex(ValueError, "Item Milk not found in inventory"):
            self.store.remove_item("Milk", 1)
    def test_remove_item_negative_quantity(self):
        self.store.add_item("Candy", 5)
        with self.assertRaisesRegex(ValueError, "Quantity to remove cannot be negative"):
            self.store.remove_item("Candy", -1)
    def test_get_inventory_empty(self):
        self.assertEqual(self.store.get_inventory(), {})
    def test_complex_scenario(self):
        self.store.add_item("A", 100)
        self.store.add_item("B", 50)
        self.store.remove_item("A", 30)
        self.store.add_item("B", 20)
        self.store.remove_item("B", 60)
        expected = {"A": 70}
        self.assertEqual(self.store.get_inventory(), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)