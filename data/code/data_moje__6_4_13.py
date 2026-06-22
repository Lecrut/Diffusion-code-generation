import unittest

def calculate_weight_difference(initial_weight, final_weight):
    return initial_weight - final_weight

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(80, 70), 10)

    def test_zero_difference(self):
        self.assertEqual(calculate_weight_difference(50, 50), 0)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(60, 70), -10)

    def test_negative_initial_weight(self):
        self.assertEqual(calculate_weight_difference(-10, 5), -15)

    def test_negative_final_weight(self):
        self.assertEqual(calculate_weight_difference(10, -5), 15)

    def test_both_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-20, -10), -10)

    def test_large_weights(self):
        self.assertEqual(calculate_weight_difference(1000, 2000), -1000)

if __name__ == '__main__':
    sample_initial = 100
    sample_final = 85
    result = calculate_weight_difference(sample_initial, sample_final)
    print(result)
    unittest.main()