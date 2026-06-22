import unittest

class Triangle:

    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Side lengths must be positive')
        if not self.is_valid_triangle(a, b, c):
            raise ValueError('Invalid triangle side lengths')
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and (b + c > a)

    def calculate_perimeter(self) -> float:
        return self.a + self.b + self.c

class TestTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.calculate_perimeter(), 12)

    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)

    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)

    def test_invalid_triangle_not_a_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)
if __name__ == '__main__':
    try:
        triangle = Triangle(3.0, 4.0, 5.0)
        print(triangle.calculate_perimeter())
        invalid_triangle = Triangle(1, 2, 3)
    except ValueError as e:
        print(e)