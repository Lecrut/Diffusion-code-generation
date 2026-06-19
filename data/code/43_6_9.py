import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_small_decimal_side(self):
        side = 3.14
        expected = round(side ** 2, 6)
        result = calculate_square_area(side)
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    # Sample values for manual testing if run directly without unittest discovery
    test_cases = [
        (4.0, 16),
        (-2, 4),  # Negative side length mathematically valid in Python but physically invalid; function still computes square
        (7, 49)
    ]

    print("Running manual sample tests...")
    for input_val, expected_output in test_cases:
        result = calculate_square_area(input_val)
        status = "PASS" if abs(result - expected_output) < 0.01 else f"FAIL (Expected {expected_output}, got {result})"
        print(f"f(calculate_square_area({input_val})) == {status}")

    # Run the official unit tests suite for comprehensive verification
    unittest.main(exit=False, verbosity=2)