import unittest

def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return side * side

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(2.5), 6.25)

    def test_negative_number(self):
        self.assertEqual(calculate_square_area(-4), 16)

    def test_zero(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_invalid_input_string(self):
        with self.assertRaises(ValueError):
            calculate_square_area("a")

    def test_invalid_input_list(self):
        with self.assertRaises(ValueError):
            calculate_square_area([1, 2])

if __name__ == '__main__':
    try:
        area1 = calculate_square_area(7)
        print(f"Area of square with side 7: {area1}")
        area2 = calculate_square_area(3.3)
        print(f"Area of square with side 3.3: {area2}")
        calculate_square_area("invalid")
    except ValueError as e:
        print(f"Error caught: {e}")

    unittest.main(argv=[''], exit=False)