import unittest

def calculate_weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Weights must be numbers")
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_negative_inputs(self):
        self.assertEqual(calculate_weight_difference(-10, -5), 5)

    def test_mixed_signs(self):
        self.assertEqual(calculate_weight_difference(-5, 5), 10)

    def test_equal_weights(self):
        self.assertEqual(calculate_weight_difference(5, 5), 0)

    def test_float_weights(self):
        self.assertAlmostEqual(calculate_weight_difference(5.5, 2.2), 3.3)

    def test_negative_float_weights(self):
        self.assertAlmostEqual(calculate_weight_difference(-5.5, -2.2), 3.3)

    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_large_weights(self):
        self.assertEqual(calculate_weight_difference(1000000, 500000), 500000)

    def test_type_error_string(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 5)

    def test_type_error_none(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(None, 5)

    def test_reversed_order(self):
        self.assertEqual(calculate_weight_difference(5, 10), 5)

if __name__ == '__main__':
    print(calculate_weight_difference(10, 5))
    print(calculate_weight_difference(-10, -5))
    print(calculate_weight_difference(-5, 5))
    print(calculate_weight_difference(5.5, 2.2))
    unittest.main(exit=False, verbosity=2)