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
        self.assertEqual(self.find_minimum([10, 3, 7, 1]), 1)
        self.assertEqual(self.find_minimum([5]), 5)
    def test_negative_numbers(self):
        self.assertEqual(self.find_minimum([-10, -5, -20, -1]), -20)
        self.assertEqual(self.find_minimum([-5, -1, -10]), -10)
        self.assertEqual(self.find_minimum([-1]), -1)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_minimum([5, -2, 8, -10]), -10)
        self.assertEqual(self.find_minimum([-5, 0, 5, -1]), -5)
        self.assertEqual(self.find_minimum([3, -1, 4, -2]), -2)
    def test_list_with_duplicates(self):
        self.assertEqual(self.find_minimum([5, 5, 2, 5]), 2)
        self.assertEqual(self.find_minimum([-3, -1, -3, 0]), -3)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            self.find_minimum([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)