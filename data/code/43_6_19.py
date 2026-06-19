import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    def test_positive_integer_side(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_float_side(self):
        self.assertAlmostEqual(calculate_square_area(3.14), 9.8596, places=4)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-2)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (no user input required)
    side = 4.5
    expected_area = 20.25

    result = calculate_square_area(side)

    print(f"Side length: {side}")
    print(f"Calculated area: {result}")
    
    # Verify against sample value manually for immediate feedback in script run
    if abs(result - expected_area) < 1e-6:
        print("Sample verification PASSED.")
    else:
        print("Sample verification FAILED.")

    # Run the unit tests automatically when executed as a module
    unittest.main(exit=False, verbosity=0)