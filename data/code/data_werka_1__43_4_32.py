import unittest

def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError('Input must be a numeric value.')
    return side * side

class TestCalculateSquareArea(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(2.5), 6.25)

    def test_zero(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_number(self):
        self.assertEqual(calculate_square_area(-4), 16)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_square_area('a')
if __name__ == '__main__':
    try:
        side_length = 7
        area_result = calculate_square_area(side_length)
        print(f'Area of square with side {side_length}: {area_result}')
        side_length_float = 8.2
        area_result_float = calculate_square_area(side_length_float)
        print(f'Area of square with side {side_length_float}: {area_result_float}')
        calculate_square_area('invalid')
    except ValueError as e:
        print(f'Error caught: {e}')
    unittest.main(argv=[''], exit=False)