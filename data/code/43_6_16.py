import unittest

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The area of the square.
        
    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):

    def test_positive_side_lengths(self):
        self.assertEqual(calculate_square_area(5), 25)
        self.assertAlmostEqual(calculate_square_area(1.5), 2.25, places=6)
        
    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    
if __name__ == '__main__':
    # Run a quick manual check with hard-coded sample values first (optional demonstration)
    print("Manual verification:")
    side = 4.5
    expected_manual = calculate_square_area(side)
    print(f"Area of square with side {side}: {expected_manual}")

    # Execute the unit tests suite
    if __name__ == '__main__':
        unittest.main()