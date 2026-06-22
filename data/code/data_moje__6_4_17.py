def calculate_weight_difference(weight_before, weight_after):
    if not isinstance(weight_before, (int, float)) or not isinstance(weight_after, (int, float)):
        raise TypeError("Inputs must be numbers")
    if weight_before < 0 or weight_after < 0:
        raise ValueError("Weights cannot be negative")
    return weight_before - weight_after

import unittest

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        result = calculate_weight_difference(100, 90)
        self.assertEqual(result, 10)

    def test_negative_difference(self):
        result = calculate_weight_difference(90, 100)
        self.assertEqual(result, -10)

    def test_zero_difference(self):
        result = calculate_weight_difference(50, 50)
        self.assertEqual(result, 0)

    def test_negative_input_weight_before(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, 50)

    def test_negative_input_weight_after(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(50, -10)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("100", 90)

    def test_decimal_inputs(self):
        result = calculate_weight_difference(100.5, 90.25)
        self.assertAlmostEqual(result, 10.25)

if __name__ == '__main__':
    print(calculate_weight_difference(75.5, 70.0))
    print(calculate_weight_difference(150, 160))
    print(calculate_weight_difference(200, 200))
    unittest.main()