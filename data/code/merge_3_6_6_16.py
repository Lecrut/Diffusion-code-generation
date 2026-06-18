import unittest

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """Calculate the absolute difference between two weights.
    
    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between weight1 and weight2.
        
    Raises:
        TypeError: If either input is not a number.
    """
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    
    return abs(weight1 - weight2)

class TestWeightDifference(unittest.TestCase):
    def test_positive_values(self):
        """Test with two positive numbers."""
        self.assertEqual(calculate_weight_difference(10.5, 4.2), 6.3)

    def test_negative_input(self):
        """Test handling of negative inputs."""
        result = calculate_weight_difference(-5.0, -10.0)
        self.assertEqual(result, 5.0)

    def test_mixed_signs(self):
        """Test with one positive and one negative number."""
        self.assertEqual(calculate_weight_difference(3.7, -2.8), 6.5)

    def test_zero_input(self):
        """Test when one of the weights is zero."""
        self.assertEqual(calculate_weight_difference(0.0, 100.0), 100.0)

    def test_identical_values(self):
        """Test when both inputs are identical."""
        result = calculate_weight_difference(42.5, 42.5)
        self.assertEqual(result, 0.0)

    def test_float_precision(self):
        """Test with floating-point numbers that have decimal precision."""
        a = 13.789
        b = 9.123
        result = calculate_weight_difference(a, b)
        expected = abs(13.789 - 9.123)
        self.assertAlmostEqual(result, expected, places=5)

    def test_type_error_int(self):
        """Test raising error when first input is not numeric."""
        with self.assertRaises(TypeError):
            calculate_weight_difference("ten", 5)

    def test_type_error_float_string(self):
        """Test raising error when second input is a string representing number."""
        with self.assertRaises(TypeError):
            calculate_weight_difference(10, "five")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction
    print("Running unit tests...")
    
    # Sample execution of the function before running test suite
    weight_a = -5.5
    weight_b = 10.2
    
    diff = calculate_weight_difference(weight_a, weight_b)
    print(f"Weight difference between {weight_a} and {weight_b}: {diff}")
    
    # Run tests with sample data embedded in test methods as per requirements
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed. Please review the output above.")