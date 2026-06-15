import unittest
def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
class TestFindSmallest(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_smallest([5, 2, 8, 1]), 1)
    def test_negative_numbers(self):
        self.assertEqual(find_smallest([-5, -10, -2, -8]), -10)
    def test_mixed_numbers(self):
        self.assertEqual(find_smallest([10, -5, 3, -1]), -5)
    def test_list_with_one_element(self):
        self.assertEqual(find_smallest([42]), 42)
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_smallest([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)