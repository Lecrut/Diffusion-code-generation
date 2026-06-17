import unittest
def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
class TestRangeCalculator(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_range([1, 5, 2, 8]), 7)
    def test_empty_list(self):
        self.assertEqual(calculate_range([]), 0)
    def test_single_element(self):
        self.assertEqual(calculate_range([10]), 0)
    def test_negative_numbers(self):
        self.assertEqual(calculate_range([-5, -2, -8]), 6)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_range([-10, 0, 5, -3]), 13)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)