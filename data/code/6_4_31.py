import unittest

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

class TestCalculateWeightDifference(unittest.TestCase):
    def test_positive_weights(self):
        self.assertEqual(calculate_weight_difference(50, 30), 20)
    
    def test_negative_weights(self):
        self.assertEqual(calculate_weight_difference(-50, -30), 20)
    
    def test_mixed_signs(self):
        self.assertEqual(calculate_weight_difference(50, -30), 80)
    
    def test_zero_weights(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)
    
    def test_same_weights(self):
        self.assertEqual(calculate_weight_difference(100, 100), 0)
    
    def test_large_numbers(self):
        self.assertEqual(calculate_weight_difference(1000000, 999999), 1)

if __name__ == '__main__':
    sample_weight1 = 75
    sample_weight2 = 30
    result = calculate_weight_difference(sample_weight1, sample_weight2)
    print(result)