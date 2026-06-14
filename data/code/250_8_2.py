import unittest
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
class TestAverageCalculation(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    def test_negative_numbers(self):
        self.assertAlmostEqual(calculate_average([-1, -2, -3]), -2.0)
    def test_mixed_numbers(self):
        self.assertAlmostEqual(calculate_average([10, 20, -5, 15]), 10.0)
    def test_single_element(self):
        self.assertEqual(calculate_average([42]), 42.0)
    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)
    def test_with_floats(self):
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)