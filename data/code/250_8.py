import unittest
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
class TestAverageCalculation(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    def test_with_negatives(self):
        self.assertAlmostEqual(calculate_average([-1, 1, 5, -3]), 1.0)
    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)
    def test_single_element(self):
        self.assertEqual(calculate_average([42]), 42.0)
    def test_floating_point_result(self):
        self.assertAlmostEqual(calculate_average([1, 2, 2, 3]), 2.0)
    def test_large_numbers(self):
        self.assertAlmostEqual(calculate_average([100, 200, 300]), 200.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)