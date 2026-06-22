import unittest

def calculate_weight_difference(base_weight, new_weight):
    return new_weight - base_weight

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(50, 60), 10)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(60, 50), -10)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(50, 50), 0)

    def test_negative_base_weight(self):
        self.assertEqual(calculate_weight_difference(-50, -40), 10)

    def test_negative_new_weight(self):
        self.assertEqual(calculate_weight_difference(50, 40), -10)

    def test_both_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-100, -50), 50)

    def test_float_weights(self):
        self.assertAlmostEqual(calculate_weight_difference(50.5, 51.2), 0.7)

if __name__ == '__main__':
    sample_base = 70.5
    sample_new = 68.2
    result = calculate_weight_difference(sample_base, sample_new)
    print(result)
    unittest.main()