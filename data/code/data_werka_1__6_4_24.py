import unittest

def calculate_weight_difference(weight1, weight2):
    if weight1 < 0 or weight2 < 0:
        raise ValueError("Weights cannot be negative")
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(50, 30), 20)
        self.assertEqual(calculate_weight_difference(70, 70), 0)
    
    def test_negative_weights(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, 20)
        with self.assertRaises(ValueError):
            calculate_weight_difference(15, -5)
    
    def test_mixed_weights(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, -20)
    
    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)
        self.assertEqual(calculate_weight_difference(0, 50), 50)
        self.assertEqual(calculate_weight_difference(50, 0), 50)

if __name__ == '__main__':
    sample_weight1 = 80
    sample_weight2 = 45
    try:
        result = calculate_weight_difference(sample_weight1, sample_weight2)
        print(f"The weight difference between {sample_weight1} and {sample_weight2} is: {result}")
    except ValueError as e:
        print(e)

    unittest.main(argv=[''], exit=False)