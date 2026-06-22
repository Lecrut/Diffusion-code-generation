import unittest

def calculate_weight_difference(weight_a, weight_b):
    if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
        raise TypeError("Weights must be numeric types.")
    return weight_a - weight_b

class TestWeightDifference(unittest.TestCase):
    def test_normal_case(self):
        result = calculate_weight_difference(10.5, 5.0)
        self.assertEqual(result, 5.5)

    def test_negative_input_b(self):
        result = calculate_weight_difference(10, -5)
        self.assertEqual(result, 15)

    def test_negative_input_a(self):
        result = calculate_weight_difference(-10, 5)
        self.assertEqual(result, -15)

    def test_both_negative(self):
        result = calculate_weight_difference(-10.0, -20.0)
        self.assertEqual(result, 10.0)

    def test_zero_weights(self):
        result = calculate_weight_difference(0, 0)
        self.assertEqual(result, 0)

    def test_zero_weight_a(self):
        result = calculate_weight_difference(0, 5)
        self.assertEqual(result, -5)

    def test_zero_weight_b(self):
        result = calculate_weight_difference(5, 0)
        self.assertEqual(result, 5)

    def test_equal_weights(self):
        result = calculate_weight_difference(100, 100)
        self.assertEqual(result, 0)

    def test_integer_inputs(self):
        result = calculate_weight_difference(10, 3)
        self.assertEqual(result, 7)

    def test_float_inputs(self):
        result = calculate_weight_difference(1.234, 0.456)
        self.assertAlmostEqual(result, 0.778)

    def test_large_numbers(self):
        result = calculate_weight_difference(1000000, 0)
        self.assertEqual(result, 1000000)

    def test_small_numbers(self):
        result = calculate_weight_difference(0.001, 0.0001)
        self.assertAlmostEqual(result, 0.0009)

    def test_string_input_raises_error(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 5)

    def test_none_input_raises_error(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(None, 5)

    def test_list_input_raises_error(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference([10], 5)

if __name__ == '__main__':
    a = 10.0
    b = 4.5
    diff = calculate_weight_difference(a, b)
    print(diff)