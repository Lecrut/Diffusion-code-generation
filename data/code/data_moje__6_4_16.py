import unittest

def calculate_weight_difference(original_weight, new_weight):
    if new_weight > original_weight:
        return new_weight - original_weight
    elif new_weight < original_weight:
        return -(original_weight - new_weight)
    else:
        return 0

class TestWeightDifference(unittest.TestCase):

    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(100, 110), 10)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(110, 100), -10)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(100, 100), 0)

    def test_negative_original_weight(self):
        self.assertEqual(calculate_weight_difference(-100, -90), 10)

    def test_negative_new_weight(self):
        self.assertEqual(calculate_weight_difference(-90, -100), -10)

    def test_both_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-100, -110), -10)

    def test_mixed_sign_weights(self):
        self.assertEqual(calculate_weight_difference(-10, 10), 20)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_weight_difference(100.5, 110.5), 10.0)

    def test_zero_original_weight(self):
        self.assertEqual(calculate_weight_difference(0, 5), 5)

    def test_zero_new_weight(self):
        self.assertEqual(calculate_weight_difference(5, 0), -5)
if __name__ == '__main__':
    result = calculate_weight_difference(100, 110)
    print(result)
    unittest.main()