import unittest

class Square:
    def __init__(self, side):
        if not isinstance(side, (int, float)):
            raise ValueError("Input must be a numeric value.")
        self.side = side

    def area(self):
        return self.side * self.side

def calculate_square_area(side):
    square = Square(side)
    return square.area()

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(calculate_square_area(5), 25)
        self.assertEqual(calculate_square_area(10.5), 110.25)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_square_area("a")

if __name__ == '__main__':
    try:
        result1 = calculate_square_area(7)
        print(f"Area of square with side 7: {result1}")
        result2 = calculate_square_area(3.5)
        print(f"Area of square with side 3.5: {result2}")
        calculate_square_area("invalid")
    except ValueError as e:
        print(f"Error caught: {e}")