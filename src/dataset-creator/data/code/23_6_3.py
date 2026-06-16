import unittest
class ItemStore:
    def __init__(self):
        self._items = {}
    @property
    def items(self) -> dict[str, str]:
        return self._items.copy()
    def add_item(self, name: str, value: int | float) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError("Value must be a positive number")
        self._items[name] = value
    def get_item(self, name: str) -> int | float:
        return self._items.get(name)
class TestItemStore(unittest.TestCase):
    def setUp(self):
        self.store = ItemStore()
    def test_add_valid_items(self):
        self.store.add_item("apple", 1.50)
        self.store.add_item("banana", 2.75)
        expected = {"apple": 1.5, "banana": 2.75}
        self.assertEqual(self.store.items, expected)
    def test_get_existing_item(self):
        self.store.add_item("orange", 3.0)
        result = self.store.get_item("orange")
        self.assertEqual(result, 3.0)
    def test_add_invalid_name_type(self):
        with self.assertRaises(TypeError):
            self.store.add_item(123, 5.0)
    def test_add_negative_value(self):
        with self.assertRaises(ValueError):
            self.store.add_item("grape", -5.0)
if __name__ == '__main__':
    unittest.main()