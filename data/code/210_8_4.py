import unittest
def calculate_range(data):
    if not data:
        return 0
    return max(data) - min(data)
class TestCalculateRange(unittest.TestCase):
    def test_standard_positive_numbers(self):
        self.assertEqual(calculate_range([1, 2, 3, 4, 5]), 4)
    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(calculate_range([-5, 0, 5, 10]), 15)
    def test_all_negative_numbers(self):
        self.assertEqual(calculate_range([-10, -5, -1]), 9)
    def test_single_element(self):
        self.assertEqual(calculate_range([7]), 0)
    def test_empty_list(self):
        self.assertEqual(calculate_range([]), 0)
    def test_with_duplicates(self):
        self.assertEqual(calculate_range([1, 5, 2, 5, 1]), 4)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)