"""Module to calculate the area of a square."""

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a given square side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side_length is negative or not a number.
    """
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative numeric value.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for verification without user input.
    import unittest
    
    class TestSquareArea(unittest.TestCase):
        
        def test_positive_integer_side(self):
            """Test with positive integer side length."""
            self.assertEqual(calculate_square_area(3), 9)
            
        def test_positive_float_side(self):
            """Test with positive float side length."""
            result = calculate_square_area(4.5)
            expected = 20.25
            self.assertAlmostEqual(result, expected)
            
        def test_zero_side_length(self):
            """Test with zero side length."""
            self.assertEqual(calculate_square_area(0), 0)
            
        def test_negative_side_raises_error(self):
            """Ensure negative input raises ValueError."""
            with self.assertRaises(ValueError):
                calculate_square_area(-5)

    if __name__ == '__main__':
        unittest.main()