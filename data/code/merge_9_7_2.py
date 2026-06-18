import unittest
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
class TestAverageCalculator(unittest.TestCase):
    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        expected_average = 3.0
        self.assertEqual(calculate_average(numbers), expected_average)
    def test_negative_numbers(self):
        numbers = [-10, -20, -30]
        expected_average = -20.0
        self.assertEqual(calculate_average(numbers), expected_average)
    def test_mixed_numbers(self):
        numbers = [-1, 1, 5, -3]
        expected_average = 1.0
        self.assertEqual(calculate_average(numbers), expected_average)
    def test_empty_list(self):
        numbers = []
        expected_average = 0
        self.assertEqual(calculate_average(numbers), expected_average)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)