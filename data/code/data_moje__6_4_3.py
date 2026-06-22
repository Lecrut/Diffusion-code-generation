def calculate_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    return abs(weight1 - weight2)

import unittest

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)
        self.assertEqual(calculate_weight_difference(5, 10), 5)
        self.assertEqual(calculate_weight_difference(10, 10), 0)

    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)
        self.assertEqual(calculate_weight_difference(0, 5), 5)
        self.assertEqual(calculate_weight_difference(5, 0), 5)

    def test_negative_weight_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-1, 5)
        with self.assertRaises(ValueError):
            calculate_weight_difference(5, -1)
        with self.assertRaises(ValueError):
            calculate_weight_difference(-1, -5)

    def test_float_weights(self):
        self.assertAlmostEqual(calculate_weight_difference(10.5, 5.2), 5.3)
        self.assertAlmostEqual(calculate_weight_difference(5.2, 10.5), 5.3)

    def test_large_weights(self):
        self.assertEqual(calculate_weight_difference(1000000, 999999), 1)

if __name__ == '__main__':
    print(calculate_weight_difference(10, 3))
    print(calculate_weight_difference(3, 10))
    print(calculate_weight_difference(5, 5))
    print(calculate_weight_difference(0, 0))
    unittest.main(argv=['first-arg-is-ignored'], exit=False)