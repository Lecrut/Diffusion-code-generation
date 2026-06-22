import unittest

def calculate_weight_difference(weight1, weight2):
    return weight1 - weight2

class TestCalculateWeightDifference(unittest.TestCase):

    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-10, -5), -5)

    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_negative_first_weight(self):
        self.assertEqual(calculate_weight_difference(-5, 5), -10)

    def test_negative_second_weight(self):
        self.assertEqual(calculate_weight_difference(5, -5), 10)

    def test_large_values(self):
        self.assertEqual(calculate_weight_difference(1000000, 0), 1000000)

    def test_float_values(self):
        self.assertAlmostEqual(calculate_weight_difference(1.5, 0.5), 1.0)

if __name__ == '__main__':
    result1 = calculate_weight_difference(100, 80)
    print(result1)
    result2 = calculate_weight_difference(-50, 50)
    print(result2)
    unittest.main()