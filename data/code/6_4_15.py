import unittest

def calculate_weight_difference(initial_weight, final_weight):
    if not isinstance(initial_weight, (int, float)) or not isinstance(final_weight, (int, float)):
        raise TypeError("Weights must be numbers")
    if initial_weight < 0 or final_weight < 0:
        raise ValueError("Weights cannot be negative")
    return final_weight - initial_weight

def run_samples():
    sample_initial = 75.5
    sample_final = 72.0
    result = calculate_weight_difference(sample_initial, sample_final)
    print(result)

class TestWeightDifference(unittest.TestCase):
    def test_loss(self):
        self.assertEqual(calculate_weight_difference(100, 90), -10)

    def test_gain(self):
        self.assertEqual(calculate_weight_difference(50, 55), 5)

    def test_no_change(self):
        self.assertEqual(calculate_weight_difference(80, 80), 0)

    def test_negative_initial(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, 20)

    def test_negative_final(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(10, -5)

    def test_both_negative(self):
        with self.assertRaises(ValueError):
            calculate_weight_difference(-10, -20)

    def test_string_input_initial(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference("heavy", 50)

    def test_string_input_final(self):
        with self.assertRaises(TypeError):
            calculate_weight_difference(50, "light")

if __name__ == '__main__':
    run_samples()
    unittest.main()