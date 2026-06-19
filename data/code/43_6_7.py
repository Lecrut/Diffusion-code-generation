import unittest

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer_side(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_float_side(self):
        self.assertAlmostEqual(calculate_square_area(3.14), 9.8596, places=4)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-2)

if __name__ == '__main__':
    # Run tests using hard-coded sample values within the framework itself.
    unittest.main()