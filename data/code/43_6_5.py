import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)
        
    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)
        
    def test_float_decimal(self):
        self.assertAlmostEqual(calculate_square_area(4.5), 20.25)

    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)