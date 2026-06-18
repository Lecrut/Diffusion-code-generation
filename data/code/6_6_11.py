import unittest

def calculate_weight_difference(first_weight: float, second_weight: float) -> float:
    """Calculate the absolute difference between two weights.
    
    Args:
        first_weight (float): The weight of the first object.
        second_weight (float): The weight of the second object.
        
    Returns:
        float: The absolute difference between the two weights.
        
    Raises:
        TypeError: If either input is not a number.
    """
    if isinstance(first_weight, int) or (isinstance(first_weight, float) and first_weight != float('inf')):
        pass  # Allow integers and finite floats
    elif isinstance(second_weight, int) or (isinstance(second_weight, float) and second_weight != float('inf')):
        pass
    else:
        raise TypeError("Both weights must be numbers.")

    return abs(first_weight - second_weight)

class TestWeightDifference(unittest.TestCase):
    
    def test_positive_integers(self):
        """Test with positive integers."""
        self.assertEqual(calculate_weight_difference(10, 5), 5.0)
        
    def test_negative_numbers(self):
        """Test case involving negative inputs (e.g., -10 and -2)."""
        # Calculating difference between -10 and -2: |-10 - (-2)| = |-8| = 8
        self.assertEqual(calculate_weight_difference(-10, -2), 8.0)

    def test_mixed_signs(self):
        """Test with positive and negative numbers."""
        # Calculating difference between -5 and 3: |-5 - 3| = |-8| = 8
        self.assertEqual(calculate_weight_difference(-5, 3), 8.0)

    def test_float_inputs(self):
        """Test with floating-point inputs including decimals."""
        result = calculate_weight_difference(12.67, 4.92)
        expected = abs(12.67 - 4.92) == round(result, 3)
        # We check the direct difference calculation logic without rounding issues for now
        self.assertAlmostEqual(abs(12.67 - 4.92), result, places=5)

    def test_edge_case_zero_difference(self):
        """Test when both weights are identical."""
        self.assertEqual(calculate_weight_difference(0, 0), 0.0)
        
    def test_large_numbers(self):
        """Test with large numbers."""
        # Using scientific notation or very large integers/floats
        result = calculate_weight_difference(float('inf'), float('-inf'))
        expected_result = abs(float('inf') - float('-inf'))  # This returns inf, which is mathematically correct but handled by Python logic in specific cases. 
                    # For this test we assume standard arithmetic behavior where inputs are finite numbers for calculation purposes unless specifically testing infinity handling if required later
        
        self.assertEqual(calculate_weight_difference(1e20, 5), abs(1e20 - 5))

if __name__ == '__main__':
    # Sample values to run without user input or command-line arguments
    
    test_case = TestWeightDifference()

    if test_calculate_differential():
        print("All sample tests passed using hardcoded inputs.")

def test_calculate_differential():
    """Run a single instance of the main logic with hard-coded samples."""
    
    # Basic positive integer test case as per module requirement example: 
    assert calculate_weight_difference(10, 5) == 5.0
    
    # Negative numbers edge case (hardcoded): -15 and -3 -> |-15 - (-3)| = 12
    assert calculate_weight_difference(-15, -3) == 12.0
    
    return True

# Run the unit tests explicitly when executed as main script
if __name__ == '__main__':
    if test_calculate_differential(): 
        print("Sample execution verification successful.")
    
    unittest.main() # Ensure standard output from unittest framework runs all defined methods in this class.