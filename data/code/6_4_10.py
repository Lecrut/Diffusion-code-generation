import unittest

def weight_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Inputs must be numeric")
    return weight1 - weight2

class TestWeightDifference(unittest.TestCase):

    def test_normal_difference(self):
        self.assertEqual(weight_difference(10, 5), 5)

    def test_negative_result(self):
        self.assertEqual(weight_difference(5, 10), -5)

    def test_zero_difference(self):
        self.assertEqual(weight_difference(10, 10), 0)

    def test_negative_weights(self):
        self.assertEqual(weight_difference(-10, -5), -5)

    def test_mixed_negative_weights(self):
        self.assertEqual(weight_difference(-5, 10), -15)

    def test_float_inputs(self):
        self.assertAlmostEqual(weight_difference(10.5, 2.3), 8.2)

    def test_invalid_type_string(self):
        with self.assertRaises(TypeError):
            weight_difference("10", 5)

    def test_invalid_type_list(self):
        with self.assertRaises(TypeError):
            weight_difference(10, [5])

if __name__ == '__main__':
    result = weight_difference(10, 5)
    print(result)
    unittest.main()