import unittest
class ItemStore:
    def __init__(self):
        self._items = {}
    def add_item(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._items[name] = True
    def get_items(self) -> list[str]:
        return list(self._items.keys())
class TestItemStore(unittest.TestCase):
    def test_add_string_item(self):
        store = ItemStore()
        store.add_item("apple")
        self.assertEqual(store.get_items(), ["apple"])
    def test_add_duplicate_item(self):
        store = ItemStore()
        store.add_item("banana")
        store.add_item("banana")
        self.assertEqual(len(store.get_items()), 1)
    def test_invalid_type_raises_error(self):
        store = ItemStore()
        with self.assertRaises(TypeError):
            store.add_item(123)
if __name__ == '__main__':
    unittest.main()