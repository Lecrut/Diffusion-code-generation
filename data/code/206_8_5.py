import unittest
class TestMinFunction(unittest.TestCase):
    def find_minimum(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum
    def test_positive_numbers(self):
        self.assertEqual(self.find_minimum([5, 2, 8, 1]), 1)
        self.assertEqual(self.find_minimum([10, 20, 30]), 10)
    def test_negative_numbers(self):
        self.assertEqual(self.find_minimum([-5, -1, -10, -3]), -10)
        self.assertEqual(self.find_minimum([-100, -50, -200]), -200)
        self.assertEqual(self.find_minimum([-1, -2, -3]), -3)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_minimum([5, -2, 8, -10]), -10)
        self.assertEqual(self.find_minimum([100, 0, -50, 25]), -50)
    def test_single_element(self):
        self.assertEqual(self.find_minimum([42]), 42)
        self.assertEqual(self.find_minimum([-10]), -10)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "List cannot be empty"):
            self.find_minimum([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)