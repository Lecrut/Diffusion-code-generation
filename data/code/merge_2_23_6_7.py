import unittest
class ItemNameStorage:
    def __init__(self):
        self._items = {}
    def add(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings.")
        self._items[name] = True
    def get_all_names(self) -> list[str]:
        return list(self._items.keys())
    def remove(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item names must be strings.")
        return self._items.pop(name, False)
class TestItemNameStorage(unittest.TestCase):
    def setUp(self):
        self.storage = ItemNameStorage()
    def test_add_string_name(self):
        self.storage.add("apple")
        expected_names = ["apple"]
        actual_names = self.storage.get_all_names()
        self.assertEqual(sorted(actual_names), sorted(expected_names))
    def test_add_non_string_raises_error(self):
        with self.assertRaises(TypeError):
            self.storage.add(123)
    def test_remove_existing_name(self):
        self.storage.add("banana")
        result = self.storage.remove("banana")
        expected_result = True
        actual_names = self.storage.get_all_names()
        self.assertEqual(result, expected_result)
        self.assertNotIn("banana", actual_names)
    def test_remove_non_existing_name(self):
        result = self.storage.remove("orange")
        expected_result = False
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()