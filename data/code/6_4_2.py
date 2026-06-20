import unittest

def calculate_weight_difference(initial_weight, final_weight):
    return final_weight - initial_weight

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(100, 110), 10)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(110, 100), -10)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(100, 100), 0)

    def test_both_negative_inputs(self):
        self.assertEqual(calculate_weight_difference(-10, -5), 5)

    def test_initial_negative_final_positive(self):
        self.assertEqual(calculate_weight_difference(-10, 10), 20)

    def test_initial_positive_final_negative(self):
        self.assertEqual(calculate_weight_difference(10, -10), -20)

    def test_large_values(self):
        self.assertEqual(calculate_weight_difference(1000000, 1000050), 50)

    def test_float_values(self):
        self.assertAlmostEqual(calculate_weight_difference(10.5, 10.6), 0.1)

if __name__ == '__main__':
    sample_initial = 70.0
    sample_final = 65.5
    result = calculate_weight_difference(sample_initial, sample_final)
    print(result)
    unittest.main()