import unittest

def calculate_weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return abs(weight1 - weight2)

class TestWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_weight_difference(10, 5), 5)

    def test_negative_difference(self):
        self.assertEqual(calculate_weight_difference(-10, -5), 5)

    def test_mixed_signs(self):
        self.assertEqual(calculate_weight_difference(5, -5), 10)

    def test_same_values(self):
        self.assertEqual(calculate_weight_difference(10, 10), 0)

    def test_zero_values(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("10", 5)

    def test_negative_inputs(self):
        self.assertEqual(calculate_weight_difference(-10, -15), 5)

if __name__ == '__main__':
    result = calculate_weight_difference(20, 15)
    print(result)
    unittest.main()