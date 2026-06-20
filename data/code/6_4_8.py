import unittest

def calculate_weight_difference(current_weight, initial_weight):
    if initial_weight is None or current_weight is None:
        raise ValueError("Weights cannot be None")
    if initial_weight < 0:
        raise ValueError("Initial weight cannot be negative")
    if current_weight < 0:
        raise ValueError("Current weight cannot be negative")
    return current_weight - initial_weight

class TestWeightDifference(unittest.TestCase):

    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(100, 80), 20)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(50, 80), -30)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(80, 80), 0)

    def test_zero_initial_weight(self):
        self.assertEqual(calculate_weight_difference(50, 0), 50)

    def test_zero_current_weight(self):
        self.assertEqual(calculate_weight_difference(0, 50), -50)

    def test_both_zero(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_negative_initial_weight_raises(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(80, -10)

    def test_negative_current_weight_raises(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, 50)

    def test_none_initial_weight_raises(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(50, None)

    def test_none_current_weight_raises(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(None, 50)

    def test_large_values(self):
        self.assertEqual(calculate_weight_difference(1000000, 900000), 100000)

    def test_float_values(self):
        self.assertAlmostEqual(calculate_weight_difference(100.5, 50.25), 50.25)

if __name__ == '__main__':
    result = calculate_weight_difference(100, 80)
    print(result)
    unittest.main()