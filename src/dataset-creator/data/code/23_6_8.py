import unittest
class ItemNameStorage:
    def __init__(self):
        self._items = []
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._items.append(name)
    def get_items(self) -> list[str]:
        return self._items.copy()
class TestItemNameStorage(unittest.TestCase):
    def test_add_string_item(self):
        storage = ItemNameStorage()
        storage.add_item("Apple")
        self.assertEqual(storage.get_items(), ["Apple"])
    def test_add_multiple_items(self):
        storage = ItemNameStorage()
        storage.add_item("Banana")
        storage.add_item("Cherry")
        expected = ["Banana", "Cherry"]
        self.assertEqual(storage.get_items(), expected)
    def test_reject_non_string(self):
        storage = ItemNameStorage()
        with self.assertRaises(TypeError):
            storage.add_item(123)
if __name__ == '__main__':
    unittest.main()