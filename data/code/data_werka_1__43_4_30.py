import unittest

def validate_side(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a numeric value.")
    if side < 0:
        raise ValueError("Side length cannot be negative.")

def calculate_square_area(side):
    validate_side(side)
    return side * side

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(10.5), 110.25, places=2)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_square_area("a")

if __name__ == '__main__':
    try:
        result1 = calculate_square_area(7)
        print(f"Area of square with side 7: {result1}")
        result2 = calculate_square_area(3.5)
        print(f"Area of square with side 3.5: {result2}")
        calculate_square_area(-2)
    except ValueError as e:
        print(f"Error caught: {e}")

    unittest.main(argv=[''], exit=False)