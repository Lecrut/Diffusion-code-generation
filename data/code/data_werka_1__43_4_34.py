import unittest

class Square:

    def __init__(self, side):
        self.side = side

    @staticmethod
    def validate_side(side):
        if not isinstance(side, (int, float)):
            raise ValueError('Input must be a numeric value.')

    def calculate_area(self):
        return self.side * self.side
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'Area of square with side 5: {square1.calculate_area()}')
        square2 = Square(10.5)
        print(f'Area of square with side 10.5: {square2.calculate_area()}')
        invalid_square = Square('a')
    except ValueError as e:
        print(f'Error caught: {e}')

class TestSquare(unittest.TestCase):

    def test_calculate_area(self):
        self.assertEqual(Square(3).calculate_area(), 9)
        self.assertEqual(Square(4.5).calculate_area(), 20.25)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Square('a')
        with self.assertRaises(ValueError):
            Square(None)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)