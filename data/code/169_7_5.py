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
    def remove_item(self, item_name, quantity):
        if item_name not in self.inventory:
            return False
        if quantity <= 0:
            return False
        current_quantity = self.inventory[item_name]
        if current_quantity >= quantity:
            self.inventory[item_name] -= quantity
            if self.inventory[item_name] == 0:
                del self.inventory[item_name]
            return True
        else:
            return False
class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()
    def test_add_new_item(self):
        self.manager.add_item("Apple", 10)
        self.assertEqual(self.manager.get_item("Apple"), 10)
    def test_add_existing_item(self):
        self.manager.add_item("Banana", 5)
        self.manager.add_item("Banana", 7)
        self.assertEqual(self.manager.get_item("Banana"), 12)
    def test_add_zero_quantity(self):
        self.manager.add_item("Orange", 0)
        self.assertEqual(self.manager.get_item("Orange"), 0)
    def test_add_negative_quantity(self):
        self.manager.add_item("Grape", -5)
        self.assertEqual(self.manager.get_item("Grape"), 0)
    def test_empty_initial_inventory(self):
        self.assertEqual(self.manager.get_item("TestItem"), 0)
    def test_remove_existing_item(self):
        self.manager.add_item("Book", 20)
        self.assertTrue(self.manager.remove_item("Book", 5))
        self.assertEqual(self.manager.get_item("Book"), 15)
    def test_remove_all_item(self):
        self.manager.add_item("Pen", 3)
        self.assertTrue(self.manager.remove_item("Pen", 3))
        self.assertEqual(self.manager.get_item("Pen"), 0)
        self.assertNotIn("Pen", self.manager.inventory)
    def test_remove_more_than_available(self):
        self.manager.add_item("Pencil", 5)
        self.assertFalse(self.manager.remove_item("Pencil", 10))
        self.assertEqual(self.manager.get_item("Pencil"), 5)
    def test_remove_non_existent_item(self):
        self.assertFalse(self.manager.remove_item("Eraser", 1))
    def test_remove_zero_quantity(self):
        self.manager.add_item("Ruler", 10)
        self.assertFalse(self.manager.remove_item("Ruler", 0))
        self.assertEqual(self.manager.get_item("Ruler"), 10)
    def test_remove_negative_quantity(self):
        self.manager.add_item("Sharpener", 10)
        self.assertFalse(self.manager.remove_item("Sharpener", -2))
        self.assertEqual(self.manager.get_item("Sharpener"), 10)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)