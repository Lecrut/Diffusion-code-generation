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
        self.assertEqual(self.find_minimum([5, 2, 8, 1]), 1)
        self.assertEqual(self.find_minimum([10, 4, 7, 3]), 3)
        self.assertEqual(self.find_minimum([1, 2, 3, 4]), 1)
    def test_negative_numbers(self):
        self.assertEqual(self.find_minimum([-5, -10, -2, -8]), -10)
        self.assertEqual(self.find_minimum([-100, -50, -200]), -200)
        self.assertEqual(self.find_minimum([-1, -5, -3]), -5)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_minimum([10, -5, 0, 3, -1]), -5)
        self.assertEqual(self.find_minimum([-10, 5, -20, 0]), -20)
    def test_single_element(self):
        self.assertEqual(self.find_minimum([42]), 42)
        self.assertEqual(self.find_minimum([-99]), -99)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            self.find_minimum([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)