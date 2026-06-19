import unittest

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    def test_positive_integer_side(self):
        self.assertEqual(calculate_square_area(5), 25.0)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0.0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_float_side(self):
        result = calculate_square_area(4.5)
        self.assertAlmostEqual(result, 20.25)

if __name__ == '__main__':
    # Sample execution without user input or arguments
    side = 10
    area = calculate_square_area(side)
    
    print(f"Area of a square with side {side}: {area}")

    # Run unit tests if executed directly
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)