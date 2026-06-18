import unittest
class ItemNameStorage:
    def __init__(self):
        self._items = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._items[name] = True
    def get_items(self) -> list[str]:
        return list(self._items.keys())
class TestItemNameStorage(unittest.TestCase):
    def setUp(self):
        self.storage = ItemNameStorage()
    def test_add_string_item(self):
        self.storage.add_item("Apple")
        result = self.storage.get_items()
        self.assertIn("Apple", result)
    def test_add_non_string_raises_error(self):
        with self.assertRaises(TypeError):
            self.storage.add_item(123)
    def test_get_empty_list_initially(self):
        result = self.storage.get_items()
        self.assertEqual(result, [])
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)