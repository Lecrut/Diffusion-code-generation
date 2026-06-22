import unittest

def calculate_weight_difference(weight_a, weight_b):
    if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
        raise TypeError("Weights must be numbers")
    return weight_a - weight_b

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(5, 10), -5)

    def test_equal_weights(self):
        self.assertEqual(calculate_weight_difference(7, 7), 0)

    def test_negative_input_weight_a(self):
        result = calculate_weight_difference(-5, 10)
        self.assertEqual(result, -15)

    def test_negative_input_weight_b(self):
        result = calculate_weight_difference(5, -3)
        self.assertEqual(result, 8)

    def test_both_negative_inputs(self):
        result = calculate_weight_difference(-10, -4)
        self.assertEqual(result, -6)

    def test_zero_inputs(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_weight_difference(10.5, 4.2), 6.3)

    def test_invalid_type_input(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 5)

if __name__ == '__main__':
    result = calculate_weight_difference(150.5, 140.0)
    print(result)
    result_negative_a = calculate_weight_difference(-20, 30)
    print(result_negative_a)
    result_negative_b = calculate_weight_difference(20, -30)
    print(result_negative_b)
    unittest.main()