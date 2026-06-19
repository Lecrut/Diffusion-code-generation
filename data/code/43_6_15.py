import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_decimal_value(self):
        result = calculate_square_area(3.7)
        expected_rounded = round((3.7 ** 2), 1)
        # Verify calculation directly to avoid floating point rounding ambiguity in assertions
        self.assertAlmostEqual(result, 13.69, places=2)

    def test_negative_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-4)

if __name__ == '__main__':
    # Run tests immediately for verification without command-line arguments or user input
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failIfNoRecordFailures())