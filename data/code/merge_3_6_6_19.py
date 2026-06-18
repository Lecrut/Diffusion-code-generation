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
    def test_positive_values(self):
        """Test with positive numbers."""
        self.assertEqual(calculate_weight_difference(10.5, 4.3), 6.2)

    def test_negative_values(self):
        """Test with negative numbers."""
        self.assertEqual(calculate_weight_difference(-10.0, -7.0), 3.0)

    def test_mixed_signs(self):
        """Test with one positive and one negative number."""
        self.assertEqual(calculate_weight_difference(5.0, -2.0), 7.0)
        
    def test_zero_input(self):
        """Test involving zero."""
        self.assertEqual(calculate_weight_difference(0.0, 10.0), 10.0)

    def test_identical_values(self):
        """Test when both weights are the same."""
        self.assertEqual(calculate_weight_difference(5.0, 5.0), 0.0)

    def test_float_precision(self):
        """Test with floating point precision issues."""
        result = calculate_weight_difference(1.23456789, 1.23456789)
        self.assertEqual(result, 0.0)

    def test_invalid_input_type(self):
        """Test that non-numeric inputs raise TypeError."""
        with self.assertRaises(TypeError):
            calculate_weight_difference("ten", 5.0)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    samples = [
        (10, 4),          # Positive integers
        (-5, -2),         # Negative integers
        (3.14, 2.71),     # Floats with decimals
        (0, 99),          # Zero involved
        (-100, 100),      # Large magnitude difference
    ]

    print("Running sample calculations...")
    for w1, w2 in samples:
        diff = calculate_weight_difference(w1, w2)
        print(f"Difference between {w1} and {w2}: {diff}")

    # Run the unit tests automatically if executed as a script
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)