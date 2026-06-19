import unittest

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The area of the square.
        
    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_int_side(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_float_side(self):
        result = calculate_square_area(3.14)
        expected = 9.8596
        self.assertAlmostEqual(result, expected, places=4)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

if __name__ == '__main__':
    # Run tests with hard-coded sample values implicitly via the unittest framework
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.errors + result.failures)