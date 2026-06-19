import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer_side(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_float_side(self):
        side = 4.5
        expected = side ** 2
        self.assertAlmostEqual(calculate_square_area(side), expected, places=10)

if __name__ == '__main__':
    # Run tests with hard-coded sample values to verify functionality without user input or files
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failIfNoTests and "No tests were run" or None, 1)