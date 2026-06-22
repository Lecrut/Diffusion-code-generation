import unittest

def calculate_weight_difference(weight_current, weight_target):
    if not isinstance(weight_current, (int, float)) or not isinstance(weight_target, (int, float)):
        raise TypeError("Weights must be numeric")
    if weight_current < 0 or weight_target < 0:
        raise ValueError("Weights cannot be negative")
    return weight_current - weight_target

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        result = calculate_weight_difference(80, 70)
        self.assertEqual(result, 10)

    def test_zero_difference(self):
        result = calculate_weight_difference(70, 70)
        self.assertEqual(result, 0)

    def test_negative_difference(self):
        result = calculate_weight_difference(60, 70)
        self.assertEqual(result, -10)

    def test_float_values(self):
        result = calculate_weight_difference(75.5, 70.5)
        self.assertEqual(result, 5.0)

    def test_negative_input_current(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, 50)

    def test_negative_input_target(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(50, -10)

    def test_both_negative_inputs(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, -20)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("50", 70)

    def test_non_numeric_input_target(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(50, "70")

if __name__ == '__main__':
    sample_current = 100
    sample_target = 85
    result = calculate_weight_difference(sample_current, sample_target)
    print(result)
    unittest.main()