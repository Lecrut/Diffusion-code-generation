import unittest

def calculate_weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Inputs must be numbers")
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_positive_floats(self):
        self.assertAlmostEqual(calculate_weight_difference(10.5, 5.2), 5.3)

    def test_negative_inputs(self):
        self.assertEqual(calculate_weight_difference(-10, 5), 15)
        self.assertEqual(calculate_weight_difference(-5, -10), 5)
        self.assertEqual(calculate_weight_difference(-5, 5), 10)

    def test_zero_inputs(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)
        self.assertEqual(calculate_weight_difference(5, 0), 5)

    def test_same_inputs(self):
        self.assertEqual(calculate_weight_difference(5, 5), 0)
        self.assertEqual(calculate_weight_difference(-3.5, -3.5), 0)

    def test_reversed_order(self):
        self.assertEqual(calculate_weight_difference(5, 10), 5)
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_large_numbers(self):
        self.assertEqual(calculate_weight_difference(1000000, 1), 999999)

    def test_small_floats(self):
        self.assertAlmostEqual(calculate_weight_difference(0.1, 0.2), 0.1)

    def test_type_error_string(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 5)

    def test_type_error_none(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(None, 5)

if __name__ == '__main__':
    print(calculate_weight_difference(10, 5))
    print(calculate_weight_difference(-5, 5))
    print(calculate_weight_difference(0, 0))
    unittest.main(argv=[''], exit=False, verbosity=0)