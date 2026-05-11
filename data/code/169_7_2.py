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
        if quantity >= current_quantity:
            del self.inventory[item_name]
        else:
            self.inventory[item_name] -= quantity
        return True
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
    def test_update_non_existent_item(self):
        self.manager.add_item("Pears", 20)
        self.manager.add_item("Carrots", 5)
        self.assertEqual(self.manager.get_item("NonExistent"), 0)
    def test_remove_item_partial(self):
        self.manager.add_item("Milk", 100)
        result = self.manager.remove_item("Milk", 30)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_item("Milk"), 70)
    def test_remove_item_exact_quantity(self):
        self.manager.add_item("Bread", 50)
        result = self.manager.remove_item("Bread", 50)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_item("Bread"), 0)
    def test_remove_item_more_than_available(self):
        self.manager.add_item("Cheese", 10)
        result = self.manager.remove_item("Cheese", 15)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_item("Cheese"), 0)
    def test_remove_non_existent_item(self):
        self.manager.add_item("Water", 10)
        result = self.manager.remove_item("Soda", 5)
        self.assertFalse(result)
        self.assertEqual(self.manager.get_item("Water"), 10)
    def test_remove_zero_quantity(self):
        self.manager.add_item("Eggs", 10)
        result = self.manager.remove_item("Eggs", 0)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_item("Eggs"), 10)
    def test_remove_negative_quantity(self):
        self.manager.add_item("Beans", 10)
        result = self.manager.remove_item("Beans", -5)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_item("Beans"), 10)
    def test_empty_initial_inventory(self):
        self.assertEqual(self.manager.get_item("Anything"), 0)
        self.manager.remove_item("NonExistent", 1)
        self.assertFalse(self.manager.remove_item("NonExistent", 1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)