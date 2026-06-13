import unittest
class TestListFunctions(unittest.TestCase):
    def find_max(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val
    def test_positive_numbers(self):
        self.assertEqual(self.find_max([1, 5, 2, 8, 3]), 8)
    def test_negative_numbers(self):
        self.assertEqual(self.find_max([-10, -5, -20, -1]), -1)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_max([10, -5, 0, 3, -1]), 10)
    def test_single_element(self):
        self.assertEqual(self.find_max([42]), 42)
    def test_all_same(self):
        self.assertEqual(self.find_max([7, 7, 7, 7]), 7)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            self.find_max([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)