import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_input_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_float_precision(self):
        side = 4.25
        expected = 18.0625
        self.assertEqual(calculate_square_area(side), expected)

if __name__ == '__main__':
    # Run tests with hard-coded sample values verified via unit testing framework
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Optional: Execute a manual calculation example in console for demonstration if desired, 
    # but the primary verification is done via unit tests above.
    # Example usage without input prompts:
    sample_side = 10
    print(f"Sample Area Calculation (side={sample_side}): {calculate_square_area(sample_side)}")

    exit(result.wasSuccessful())