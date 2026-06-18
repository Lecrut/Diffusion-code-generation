import unittest

def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculate the absolute difference between two weights.
    
    Args:
        w1 (float): The first weight value.
        w2 (float): The second weight value.
        
    Returns:
        float: The non-negative absolute difference |w1 - w2|.
    """
    return abs(w1 - w2)

class TestWeightDifference(unittest.TestCase):

    def test_normal_positive_values(self):
        # Standard case with positive weights where result is expected to be 5.0
        self.assertEqual(calculate_weight_difference(10, 5), 5.0)

    def test_negative_inputs_edge_case_1(self):
        # Both inputs are negative; difference should still be correct (| -2 - (-8) | = |-6| = 6)
        self.assertEqual(calculate_weight_difference(-2, -8), 6.0)

    def test_mixed_positive_and_negative_inputs(self):
        # One positive and one negative input
        self.assertEqual(calculate_weight_difference(10, -5), 15.0)

    def test_zero_input_edge_case_1(self):
        # First weight is zero
        self.assertEqual(calculate_weight_difference(0, 7), 7.0)

    def test_zero_input_edge_case_2(self):
        # Second weight is zero
        self.assertEqual(calculate_weight_difference(3, 0), 3.0)

    def test_identical_values_return_zero(self):
        """Verify that identical values result in a difference of zero."""
        self.assertEqual(calculate_weight_difference(10, 10), 0.0)
        self.assertEqual(calculate_weight_difference(-5, -5), 0.0)

    def test_float_precision_edge_case(self):
        # Test with floating point numbers close to each other but not equal
        result = calculate_weight_difference(3.456789, 1.234567)
        self.assertEqual(result, 2.222222)

if __name__ == '__main__':
    # Hard-coded sample execution to verify module functionality without external input
    
    def run_samples():
        print("Running manual samples:")
        
        w1 = 50
        w2 = 30
        diff = calculate_weight_difference(w1, w2)
        print(f"Weights: {w1}, {w2} -> Difference: {diff}")

        # Edge case with negatives as per task requirement simulation
        neg_w1 = -4.5
        neg_w2 = 3.0
        diff_neg = calculate_weight_difference(neg_w1, neg_w2)
        print(f"Negative/Positive Weights: {neg_w1}, {neg_w2} -> Difference: {diff_neg}")

    run_samples()
    
    # Run the unit tests automatically after samples
    if __name__ == '__main__':
        unittest.main(exit=False)