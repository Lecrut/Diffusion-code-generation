import unittest

def calculate_weight_difference(item1: float, item2: float) -> float:
    """
    Calculate the absolute difference between two weights.
    
    Args:
        item1 (float): The first weight value.
        item2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between item1 and item2.
        
    Raises:
        TypeError: If either input is not a numeric type.
    """
    if not isinstance(item1, (int, float)) or not isinstance(item2, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    
    return abs(float(item1) - float(item2))

class TestWeightDifference(unittest.TestCase):
    def test_positive_difference(self):
        """Test with two positive weights where item1 > item2."""
        self.assertEqual(calculate_weight_difference(50.0, 30.0), 20.0)

    def test_negative_input(self):
        """Test handling of negative weight values."""
        result = calculate_weight_difference(-45.0, -78.0)
        self.assertAlmostEqual(result, 33.0)

    def test_mixed_signs(self):
        """Test with one positive and one negative weight."""
        self.assertEqual(calculate_weight_difference(10.0, -20.0), 30.0)

    def test_zero_inputs(self):
        """Test when both weights are zero or include zero."""
        self.assertEqual(calculate_weight_difference(0.0, 0.0), 0.0)
        self.assertEqual(calculate_weight_difference(-5.0, 5.0), 10.0)

    def test_integer_inputs(self):
        """Test with integer inputs instead of floats."""
        self.assertEqual(calculate_weight_difference(10, 4), 6)

    def test_float_precision(self):
        """Test floating point precision edge cases."""
        result = calculate_weight_difference(3.5, 2.75)
        self.assertAlmostEqual(result, 0.75)

if __name__ == '__main__':
    # Run tests with hard-coded sample values to ensure no external dependencies or input required
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(1)