import unittest
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
class TestFindMinimum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_minimum([5, 2, 8, 1]), 1)
        self.assertEqual(find_minimum([10, 20, 30]), 10)
        self.assertEqual(find_minimum([7]), 7)
    def test_negative_numbers(self):
        self.assertEqual(find_minimum([-5, -1, -10, -3]), -10)
        self.assertEqual(find_minimum([-10, -20, -30]), -30)
        self.assertEqual(find_minimum([-1]), -1)
    def test_mixed_numbers(self):
        self.assertEqual(find_minimum([5, -2, 8, -10]), -10)
        self.assertEqual(find_minimum([-5, 0, 5, -1]), -5)
        self.assertEqual(find_minimum([3, 1, 4, 2]), 1)
    def test_list_with_duplicates(self):
        self.assertEqual(find_minimum([5, 5, 2, 5]), 2)
        self.assertEqual(find_minimum([-1, -5, -1, -1]), -5)
    def test_single_element_list(self):
        self.assertEqual(find_minimum([42]), 42)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            find_minimum([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)