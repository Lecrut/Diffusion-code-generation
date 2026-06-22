import unittest

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def calculate_perimeter(a: float, b: float, c: float) -> float:
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle side lengths")
    return a + b + c

class TestCalculatePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(6, 8, 10), 24)

    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(0, 4, 5)

    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(-3, 4, 5)

    def test_invalid_triangle_not_a_triangle(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(1, 2, 3)

if __name__ == '__main__':
    side_a = 7.0
    side_b = 24.0
    side_c = 25.0
    try:
        perimeter = calculate_perimeter(side_a, side_b, side_c)
        print(f"The perimeter of the triangle is: {perimeter}")
    except ValueError as e:
        print(e)