import unittest

def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return side * side

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(10.5), 110.25, places=2)

    def test_negative_number(self):
        self.assertEqual(calculate_square_area(-3), 9)

    def test_zero(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_invalid_input_string(self):
        with self.assertRaises(ValueError):
            calculate_square_area("invalid")

    def test_invalid_input_list(self):
        with self.assertRaises(ValueError):
            calculate_square_area([1, 2, 3])

if __name__ == '__main__':
    try:
        result1 = calculate_square_area(7)
        print(f"Area of square with side 7: {result1}")
        result2 = calculate_square_area(3.5)
        print(f"Area of square with side 3.5: {result2}")
        calculate_square_area("a")
    except ValueError as e:
        print(f"Error caught: {e}")

    unittest.main(argv=[''], exit=False)