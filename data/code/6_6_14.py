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
        """Test case with positive weights resulting in a difference."""
        self.assertEqual(calculate_weight_difference(10.5, 4.2), 6.3)

    def test_negative_input_first(self):
        """Test case where the first weight is negative."""
        result = calculate_weight_difference(-5.0, 3.0)
        self.assertEqual(result, 8.0)

    def test_negative_input_second(self):
        """Test case where the second weight is negative."""
        result = calculate_weight_difference(7.0, -2.0)
        self.assertEqual(result, 9.0)

    def test_both_negatives(self):
        """Test case with both weights being negative."""
        result = calculate_weight_difference(-15.0, -8.0)
        self.assertEqual(result, 7.0)

    def test_zero_input(self):
        """Test case involving zero as one of the inputs."""
        self.assertEqual(calculate_weight_difference(0.0, 20.0), 20.0)
        
    def test_identical_values(self):
        """Test case where both weights are identical (difference should be zero)."""
        result = calculate_weight_difference(100.0, 100.0)
        self.assertEqual(result, 0.0)

    def test_float_precision(self):
        """Test case with floating point precision edge cases."""
        # Using values that might have representation issues in standard float arithmetic
        a = 0.1 + 0.2
        b = 0.3
        self.assertAlmostEqual(calculate_weight_difference(a, b), 0.0)

    def test_integer_inputs(self):
        """Test case ensuring integer inputs work correctly."""
        result = calculate_weight_difference(5, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or arguments
    
    # Sample test run using the function directly to show usage
    print("Sample Calculations:")
    
    normal_case = calculate_weight_difference(50.5, 20.3)
    print(f"Difference between 50.5 and 20.3: {normal_case}")
    
    negative_first = calculate_weight_difference(-10.0, 5.0)
    print(f"Difference between -10.0 and 5.0: {negative_first}")
    
    both_negative = calculate_weight_difference(-45.0, -23.0)
    print(f"Difference between -45.0 and -23.0: {both_negative}")
    
    # Run the unit tests if executed as a script
    unittest.main(verbosity=2)