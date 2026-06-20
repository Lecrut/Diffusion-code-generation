import unittest

def calculate_weight_difference(weight_1, weight_2):
    if not isinstance(weight_1, (int, float)) or not isinstance(weight_2, (int, float)):
        raise TypeError("Weights must be numbers")
    return abs(weight_1 - weight_2)

def run_sample_calculation():
    sample_a = 150.5
    sample_b = 140.0
    result = calculate_weight_difference(sample_a, sample_b)
    print(result)
    sample_c = -10
    sample_d = -20
    result_neg = calculate_weight_difference(sample_c, sample_d)
    print(result_neg)

class TestWeightDifference(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(calculate_weight_difference(100, 50), 50)
        self.assertEqual(calculate_weight_difference(50, 100), 50)

    def test_negative_numbers(self):
        self.assertEqual(calculate_weight_difference(-10, -20), 10)
        self.assertEqual(calculate_weight_difference(-20, -10), 10)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(10, 10), 0)

    def test_mixed_signs(self):
        self.assertEqual(calculate_weight_difference(10, -10), 20)

    def test_float_values(self):
        self.assertEqual(calculate_weight_difference(10.5, 10.0), 0.5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 50)

if __name__ == '__main__':
    run_sample_calculation()
    unittest.main()