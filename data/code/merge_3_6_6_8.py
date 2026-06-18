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
        """Test with positive numbers where result is expected to be non-zero."""
        self.assertEqual(calculate_weight_difference(10.5, 4.3), 6.2)

    def test_negative_difference_result(self):
        """Verify that the function returns a positive value regardless of input order."""
        self.assertEqual(calculate_weight_difference(-5.0, -9.0), 4.0)
        
    def test_zero_input(self):
        """Test scenarios involving zero values."""
        self.assertEqual(calculate_weight_difference(0.0, 10.0), 10.0)

    def test_identical_values(self):
        """Ensure the difference is zero when inputs are identical."""
        result = calculate_weight_difference(5.789, 5.789)
        self.assertEqual(result, 0.0)

    def test_negative_inputs(self):
        """Test with negative numbers to ensure correct handling of edge cases."""
        self.assertEqual(calculate_weight_difference(-12.34, -6.78), 5.56)

    def test_mixed_signs_large_values(self):
        """Verify calculation works for large positive and negative combinations."""
        result = calculate_weight_difference(1000000.5, -999999.5)
        self.assertEqual(result, 2000000.0)

    def test_float_precision(self):
        """Test floating point precision handling with specific decimal values."""
        result = calculate_weight_difference(1.3456789, 1.3456789 + 0.0000001)
        self.assertAlmostEqual(result, 0.0000001, places=7)

    def test_invalid_input_type(self):
        """Ensure TypeError is raised for non-numeric inputs."""
        with self.assertRaises(TypeError):
            calculate_weight_difference("ten", "twenty")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.errors + result.failures)