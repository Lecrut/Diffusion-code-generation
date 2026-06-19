import unittest

def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError('Input must be a numeric value.')
    return side * side

class TestSquareArea(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(2.5), 6.25, places=2)

    def test_zero(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-4)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_square_area('a')
if __name__ == '__main__':
    try:
        result1 = calculate_square_area(7)
        print(f'Area of square with side 7: {result1}')
        result2 = calculate_square_area(3.5)
        print(f'Area of square with side 3.5: {result2}')
        calculate_square_area('invalid')
    except ValueError as e:
        print(f'Error caught: {e}')
    unittest.main(argv=[''], exit=False)