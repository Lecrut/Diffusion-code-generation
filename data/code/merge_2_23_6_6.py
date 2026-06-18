import unittest
class ItemNameStorage:
    def __init__(self):
        self._items = {}
    def add(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings")
        self._items[name] = True
    def get_all_names(self) -> list[str]:
        return list(self._items.keys())
class TestItemNameStorage(unittest.TestCase):
    def setUp(self):
        self.storage = ItemNameStorage()
    def test_add_string_item(self):
        self.storage.add("Apple")
        names = self.storage.get_all_names()
        self.assertIn("Apple", names)
    def test_add_duplicate_item(self):
        self.storage.add("Banana")
        self.storage.add("Banana")
        names = self.storage.get_all_names()
        self.assertEqual(names.count("Banana"), 1)
    def test_reject_non_string_items(self):
        with self.assertRaises(TypeError):
            self.storage.add(123)
if __name__ == '__main__':
    unittest.main()