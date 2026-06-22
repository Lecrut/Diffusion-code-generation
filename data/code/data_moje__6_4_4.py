import unittest

def calculate_weight_difference(current_weight, target_weight):
    if not isinstance(current_weight, (int, float)):
        raise TypeError("current_weight must be a number")
    if not isinstance(target_weight, (int, float)):
        raise TypeError("target_weight must be a number")
    return current_weight - target_weight

class TestWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        result = calculate_weight_difference(100, 90)
        self.assertEqual(result, 10)

    def test_negative_difference(self):
        result = calculate_weight_difference(90, 100)
        self.assertEqual(result, -10)

    def test_zero_difference(self):
        result = calculate_weight_difference(100, 100)
        self.assertEqual(result, 0)

    def test_float_inputs(self):
        result = calculate_weight_difference(85.5, 80.0)
        self.assertAlmostEqual(result, 5.5)

    def test_negative_current_weight(self):
        result = calculate_weight_difference(-10, 0)
        self.assertEqual(result, -10)

    def test_negative_target_weight(self):
        result = calculate_weight_difference(0, -10)
        self.assertEqual(result, 10)

    def test_both_negative_weights(self):
        result = calculate_weight_difference(-50, -60)
        self.assertEqual(result, 10)

    def test_zero_current_weight(self):
        result = calculate_weight_difference(0, 10)
        self.assertEqual(result, -10)

    def test_zero_target_weight(self):
        result = calculate_weight_difference(10, 0)
        self.assertEqual(result, 10)

    def test_type_error_current(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("100", 90)

    def test_type_error_target(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(100, "90")

    def test_large_numbers(self):
        result = calculate_weight_difference(1000000, 1)
        self.assertEqual(result, 999999)

    def test_small_decimal_difference(self):
        result = calculate_weight_difference(1.0001, 1.0)
        self.assertAlmostEqual(result, 0.0001)

if __name__ == '__main__':
    sample_current = 250
    sample_target = 230
    difference = calculate_weight_difference(sample_current, sample_target)
    print(difference)
    unittest.main(exit=False)