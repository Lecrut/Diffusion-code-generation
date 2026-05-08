import unittest
class TestFindSmallest(unittest.TestCase):
    def find_smallest(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        smallest = data[0]
        for item in data[1:]:
            if item < smallest:
                smallest = item
        return smallest
    def test_positive_integers(self):
        self.assertEqual(self.find_smallest([5, 2, 8, 1, 9]), 1)
        self.assertEqual(self.find_smallest([10, 20, 30]), 10)
    def test_negative_numbers(self):
        self.assertEqual(self.find_smallest([-5, -1, -10, -3]), -10)
        self.assertEqual(self.find_smallest([-10, -5, -20]), -20)
    def test_mixed_numbers(self):
        self.assertEqual(self.find_smallest([5, -2, 8, -1]), -2)
        self.assertEqual(self.find_smallest([10, -5, 0, 3]), -5)
    def test_single_element_list(self):
        self.assertEqual(self.find_smallest([42]), 42)
    def test_list_with_duplicates(self):
        self.assertEqual(self.find_smallest([5, 5, 5, 5]), 5)
        self.assertEqual(self.find_smallest([10, 2, 10, 2]), 2)
        self.assertEqual(self.find_smallest([-1, 5, -1, 3]), -1)
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            self.find_smallest([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)