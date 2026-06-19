import unittest
SQUARE_AREA_MULTIPLIER = 2

def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError('Input must be a numeric value.')
    return side * side * SQUARE_AREA_MULTIPLIER

class TestCalculateSquareArea(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(3), 18)

    def test_positive_float(self):
        self.assertEqual(calculate_square_area(2.5), 12.5)

    def test_zero(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-4)

    def test_string_input(self):
        with self.assertRaises(ValueError):
            calculate_square_area('a')
if __name__ == '__main__':
    try:
        result1 = calculate_square_area(5)
        print(f'Area of square with side 5: {result1}')
        result2 = calculate_square_area(7.2)
        print(f'Area of square with side 7.2: {result2}')
        calculate_square_area('invalid')
    except ValueError as e:
        print(f'Error caught: {e}')
    unittest.main(argv=[''], exit=False)