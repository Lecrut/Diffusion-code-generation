import unittest
def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list")
    return sum(numbers) / len(numbers)
class TestCalculateMean(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_mean([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(calculate_mean([10, 20, 30], places=2), 20.0)
    def test_negative_numbers(self):
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0)
        self.assertAlmostEqual(calculate_mean([-10, 0, 10], places=2), 0.0)
    def test_mixed_numbers(self):
        self.assertEqual(calculate_mean([-1, 1, 5]), 1.6666666666666667)
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_mean([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)