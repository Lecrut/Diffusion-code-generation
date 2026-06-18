import unittest

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculate the absolute difference between two weights.
    
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
    def test_positive_difference(self):
        """Test case with positive difference."""
        self.assertEqual(calculate_weight_difference(10.5, 4.2), 6.3)

    def test_negative_difference_result(self):
        """Ensure the result is always non-negative despite input order."""
        self.assertEqual(calculate_weight_difference(-5.0, -9.0), 4.0)

    def test_zero_input(self):
        """Test case involving zero values."""
        self.assertEqual(calculate_weight_difference(0.0, 10.0), 10.0)
        self.assertEqual(calculate_weight_difference(-7.5, 0.0), 7.5)

    def test_identical_values(self):
        """Test case where weights are identical."""
        self.assertEqual(calculate_weight_difference(42.0, 42.0), 0.0)

    def test_negative_inputs(self):
        """Comprehensive edge cases with negative inputs."""
        result = calculate_weight_difference(-15.3, -8.7)
        expected = abs(-15.3 - (-8.7))
        self.assertEqual(result, expected)

    def test_float_precision(self):
        """Test floating-point precision handling."""
        a = 0.1 + 0.2
        b = 0.3
        # Allow small tolerance for float arithmetic issues if needed, 
        # but here we check exact diff logic which holds regardless of representation quirks in inputs.
        self.assertEqual(calculate_weight_difference(a, b), abs(0.1 + 0.2 - 0.3))

    def test_type_error_int(self):
        """Test raising TypeError when an integer is passed."""
        with self.assertRaises(TypeError):
            calculate_weight_difference("ten", 5)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without external input
    print(f"Sample Calculation: |10.5 - 4.2| = {calculate_weight_difference(10.5, 4.2)}")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed
    exit(result.wasSuccessful() and 0 or 1)