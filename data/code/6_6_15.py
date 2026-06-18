import unittest

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """Calculate the absolute difference between two weights.
    
    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between weight1 and weight2.
    """
    return abs(weight1 - weight2)

class TestWeightDifference(unittest.TestCase):
    
    def test_positive_integers(self):
        self.assertEqual(calculate_weight_difference(5, 3), 2)

    def test_negative_integers(self):
        # Edge case: both inputs are negative
        self.assertEqual(calculate_weight_difference(-10, -4), 6)

    def test_mixed_signs_positive_result(self):
        # Positive minus negative should yield larger positive difference
        self.assertEqual(calculate_weight_difference(5, -3), 8)

    def test_mixed_signs_negative_subtraction_order(self):
        # Negative minus positive yields same absolute result as above
        self.assertEqual(calculate_weight_difference(-5, 3), 8)

    def test_zero_inputs(self):
        self.assertEqual(calculate_weight_difference(0, 0), 0)

    def test_one_input_is_zero(self):
        self.assertEqual(calculate_weight_difference(10.5, 0), 10.5)
        
    def test_float_precision(self):
        # Test with floating point numbers that might have precision nuances
        result = calculate_weight_difference(3.456789, 2.123456)
        self.assertAlmostEqual(result, 1.333333, places=6)

    def test_large_values(self):
        # Test with large numbers to ensure no overflow issues in standard float handling
        result = calculate_weight_difference(1e9, -1e8)
        self.assertEqual(result, 1100000000.0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    
    # Hard-coded sample values execution for demonstration (not part of test cases above but runs once before tests if desired, 
    # though typically unit frameworks run the class directly. This block ensures standalone runnable behavior).
    
    print("Running manual sample calculations...")
    samples = [
        ("Normal case", 10, 5),
        ("Negative inputs", -20, -7),
        ("Mixed signs", 100, -50),
        ("Zero difference", 42.5, 42.5)
    ]

    for desc, w1, w2 in samples:
        diff = calculate_weight_difference(w1, w2)
        print(f"{desc}: |{w1} - {w2}| = {diff}")

    # Run the actual unit tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    exit(result.wasSuccessful())