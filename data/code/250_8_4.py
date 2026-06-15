import unittest
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)
class TestAverageCalculator(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    def test_negative_numbers(self):
        self.assertAlmostEqual(calculate_average([-1, -2, -3]), -2.0)
    def test_mixed_numbers(self):
        self.assertAlmostEqual(calculate_average([10, -5, 15, -10]), 2.5)
    def test_single_element(self):
        self.assertEqual(calculate_average([42]), 42.0)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            calculate_average([])
    def test_float_result(self):
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4]), 2.5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)