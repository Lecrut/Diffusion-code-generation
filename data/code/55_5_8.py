import unittest

def calculate_perimeter(a: float, b: float, c: float) -> float:
    if not all(side > 0 for side in [a, b, c]):
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle side lengths")
    return a + b + c

class TestCalculatePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(7, 10, 5), 22)

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
    side_a = 6.0
    side_b = 8.0
    side_c = 10.0
    perimeter = calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)