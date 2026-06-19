import unittest

def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The area of the square.
        
    Raises:
        ValueError: If side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):

    def test_positive_integer_side(self):
        # Hard-coded sample values as per requirements; no user input needed.
        result = calculate_square_area(5)
        self.assertEqual(result, 25)

    def test_float_side(self):
        side_length = 3.7
        expected = 13.69
        result = calculate_square_area(side_length)
        self.assertAlmostEqual(result, expected)

    def test_zero_side(self):
        result = calculate_square_area(0)
        self.assertEqual(result, 0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

if __name__ == '__main__':
    # Run the unit tests; no command-line arguments or network access required.
    unittest.main()