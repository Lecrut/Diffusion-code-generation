import unittest
class TestMinFunction(unittest.TestCase):
    def find_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum
    def test_positive_numbers(self):
        self.assertEqual(self.find_minimum([1, 5, 2, 8]), 1)
    def test_negative_numbers(self):
        self.assertEqual(self.find_minimum([-5, -1, -10, -3]), -10)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_minimum([10, -5, 20, -1]), -5)
    def test_single_element(self):
        self.assertEqual(self.find_minimum([42]), 42)
    def test_all_same_elements(self):
        self.assertEqual(self.find_minimum([7, 7, 7, 7]), 7)
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            self.find_minimum([])
    def test_list_with_zero(self):
        self.assertEqual(self.find_minimum([5, 0, -2, 1]), -2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)