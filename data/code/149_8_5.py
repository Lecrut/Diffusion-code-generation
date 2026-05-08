import unittest
class ListReverser:
    def reverse_list(self, data):
        data.reverse()
class TestListReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = ListReverser()
    def test_empty_list(self):
        data = []
        self.reverser.reverse_list(data)
        self.assertEqual(data, [])
    def test_single_element_list(self):
        data = [1]
        self.reverser.reverse_list(data)
        self.assertEqual(data, [1])
    def test_simple_list(self):
        data = [1, 2, 3, 4, 5]
        self.reverser.reverse_list(data)
        self.assertEqual(data, [5, 4, 3, 2, 1])
    def test_list_with_duplicates(self):
        data = [1, 2, 2, 3, 1]
        self.reverser.reverse_list(data)
        self.assertEqual(data, [1, 3, 2, 2, 1])
    def test_list_with_negatives(self):
        data = [-1, 0, 5, -10]
        self.reverser.reverse_list(data)
        self.assertEqual(data, [-10, 5, 0, -1])
    def test_list_with_strings(self):
        data = ["a", "b", "c", "d"]
        self.reverser.reverse_list(data)
        self.assertEqual(data, ["d", "c", "b", "a"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)