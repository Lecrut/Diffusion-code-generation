import unittest

def calculate_weight_difference(weight_before, weight_after):
    if not isinstance(weight_before, (int, float)) or not isinstance(weight_after, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return weight_before - weight_after

class TestWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(100, 80), 20)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(80, 100), -20)

    def test_equal_weights(self):
        self.assertEqual(calculate_weight_difference(50, 50), 0)

    def test_negative_inputs(self):
        self.assertEqual(calculate_weight_difference(-50, -30), -20)
        self.assertEqual(calculate_weight_difference(-30, -50), 20)
        self.assertEqual(calculate_weight_difference(-10, 10), -20)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_weight_difference(10.5, 8.5), 2.0)

    def test_mixed_negative_positive(self):
        self.assertEqual(calculate_weight_difference(-100, 100), -200)
        self.assertEqual(calculate_weight_difference(100, -100), 200)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("100", 80)

if __name__ == '__main__':
    sample_result = calculate_weight_difference(150, 120)
    print(sample_result)
    negative_input_result = calculate_weight_difference(-20, -10)
    print(negative_input_result)
    unittest.main(exit=False)