import unittest
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
class TestAverageCalculator(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4]), 2.5)
    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3, -4]), -2.5)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-10, 0, 10]), 0.0)
    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)