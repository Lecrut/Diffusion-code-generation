import unittest
def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
class TestRangeCalculator(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_range([1, 2, 3, 4, 5]), 4)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_range([10, 5, 20, 1]), 19)
    def test_empty_list(self):
        self.assertEqual(calculate_range([]), 0)
    def test_negative_numbers(self):
        self.assertEqual(calculate_range([-5, -2, -10]), 8)
    def test_all_negative_numbers(self):
        self.assertEqual(calculate_range([-10, -5, -1]), 9)
    def test_single_element(self):
        self.assertEqual(calculate_range([7]), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)