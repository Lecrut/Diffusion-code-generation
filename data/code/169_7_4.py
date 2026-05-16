import unittest
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if quantity <= 0:
            return
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def get_item(self, item_name):
        return self.inventory.get(item_name, 0)
    def update_item(self, item_name, new_quantity):
        if item_name in self.inventory:
            if new_quantity < 0:
                raise ValueError("Quantity cannot be negative")
            self.inventory[item_name] = new_quantity
        else:
            raise KeyError(f"Item '{item_name}' not found")
class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()
    def test_add_new_item(self):
        self.manager.add_item("Apples", 10)
        self.assertEqual(self.manager.get_item("Apples"), 10)
    def test_add_existing_item(self):
        self.manager.add_item("Bananas", 5)
        self.manager.add_item("Bananas", 7)
        self.assertEqual(self.manager.get_item("Bananas"), 12)
    def test_add_zero_quantity(self):
        self.manager.add_item("Oranges", 0)
        self.assertEqual(self.manager.get_item("Oranges"), 0)
    def test_add_negative_quantity(self):
        self.manager.add_item("Grapes", -5)
        self.assertEqual(self.manager.get_item("Grapes"), 0)
    def test_get_non_existent_item(self):
        self.assertEqual(self.manager.get_item("Pears"), 0)
    def test_empty_initial_inventory(self):
        self.assertEqual(self.manager.get_item("Anything"), 0)
    def test_update_existing_item(self):
        self.manager.add_item("Carrots", 20)
        self.manager.update_item("Carrots", 15)
        self.assertEqual(self.manager.get_item("Carrots"), 15)
    def test_update_to_zero(self):
        self.manager.add_item("Tomatoes", 30)
        self.manager.update_item("Tomatoes", 0)
        self.assertEqual(self.manager.get_item("Tomatoes"), 0)
    def test_update_non_existent_item(self):
        with self.assertRaises(KeyError):
            self.manager.update_item("NonExistent", 10)
    def test_update_with_negative_quantity(self):
        self.manager.add_item("Potatoes", 50)
        with self.assertRaises(ValueError):
            self.manager.update_item("Potatoes", -5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)