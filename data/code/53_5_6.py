import unittest

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

    def area(self):
        return Square.calculate_area(self.side_length)

class TestSquare(unittest.TestCase):
    def test_positive_side_length(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_zero_side_length(self):
        square = Square(0)
        self.assertEqual(square.area(), 0)

    def test_negative_side_length(self):
        square = Square(-4)
        self.assertEqual(square.area(), 16)

if __name__ == '__main__':
    sample_values = [2, 5, -3]
    for value in sample_values:
        print(f"Area of square with side length {value}: {Square.calculate_area(value)}")