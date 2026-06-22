import unittest

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):

    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(50, 30), 20)

    def test_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-50, -30), 20)

    def test_mixed_sign_weights(self):
        self.assertEqual(calculate_weight_difference(-50, 30), 80)

    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_one_zero_weight(self):
        self.assertEqual(calculate_weight_difference(0, 30), 30)
        self.assertEqual(calculate_weight_difference(50, 0), 50)

    def test_large_numbers(self):
        self.assertEqual(calculate_weight_difference(1000000, 999999), 1)
if __name__ == '__main__':
    print(calculate_weight_difference(70, 30))
    unittest.main(argv=[''], exit=False)