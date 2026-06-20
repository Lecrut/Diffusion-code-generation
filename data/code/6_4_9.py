import unittest

def calculate_weight_diff(weight1, weight2):
    if not isinstance(weight1, (int, float)):
        raise TypeError("weight1 must be a number")
    if not isinstance(weight2, (int, float)):
        raise TypeError("weight2 must be a number")
    return weight1 - weight2

class TestWeightDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_weight_diff(10, 5), 5)

    def test_negative_result(self):
        self.assertEqual(calculate_weight_diff(5, 10), -5)

    def test_negative_inputs(self):
        self.assertEqual(calculate_weight_diff(-5, -10), 5)

    def test_zero_inputs(self):
        self.assertEqual(calculate_weight_diff(0, 0), 0)

    def test_mixed_positive_negative(self):
        self.assertEqual(calculate_weight_diff(5, -5), 10)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_weight_diff(5.5, 2.3), 3.2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            calculate_weight_diff("10", 5)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            calculate_weight_diff(None, 5)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(calculate_weight_diff(100, 80))
    print(calculate_weight_diff(50, 75))
    print(calculate_weight_diff(-10, -20))