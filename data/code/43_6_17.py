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
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_float_value(self):
        result = calculate_square_area(4.5)
        self.assertAlmostEqual(result, 20.25)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (no user input required)
    side_a = 10
    expected_area_a = 100
    
    side_b = 7.5
    expected_area_b = 56.25

    print(f"Sample Test: Area of square with side {side_a} is {expected_area_a}")
    
    # Run the unit tests to verify functionality
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(1)