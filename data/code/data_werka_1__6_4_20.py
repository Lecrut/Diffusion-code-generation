import unittest

def calculate_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError('Weights must be non-negative')
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):

    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(50, 30), 20)
        self.assertEqual(calculate_weight_difference(70, 70), 0)

    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)
        self.assertEqual(calculate_weight_difference(10, 0), 10)

    def test_negative_weights(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-5, 30)
        with self.assertRaises(ValueError):
            calculate_weight_difference(20, -10)

    def test_mixed_signs(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-5, -10)
if __name__ == '__main__':
    print(calculate_weight_difference(80, 60))
    unittest.main(argv=[''], exit=False)