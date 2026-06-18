import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_input(self):
        # Geometrically invalid, but function handles it mathematically (returns positive area of magnitude)
        result = calculate_square_area(-3)
        self.assertEqual(result, 9)

    def test_float_side(self):
        self.assertAlmostEqual(calculate_square_area(4.5), 20.25)

if __name__ == '__main__':
    # Run tests with hard-coded sample values implicitly covered in the class methods
    unittest.main()