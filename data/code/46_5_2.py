import unittest

def calculate_triangle_perimeter(side_a, side_b, side_c):
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Sides must be positive")
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        raise ValueError("Invalid triangle sides")
    return side_a + side_b + side_c

class TestTrianglePerimeter(unittest.TestCase):
    def test_valid_equilateral(self):
        self.assertEqual(calculate_triangle_perimeter(3, 3, 3), 9)

    def test_valid_isosceles(self):
        self.assertEqual(calculate_triangle_perimeter(5, 5, 8), 18)

    def test_valid_scalene(self):
        self.assertEqual(calculate_triangle_perimeter(3, 4, 5), 12)

    def test_invalid_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(-1, 2, 3)

    def test_invalid_zero_side(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(0, 5, 5)

    def test_invalid_triangle_inequality(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(1, 2, 10)

    def test_invalid_triangle_inequality_equal_sum(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(1, 2, 3)

if __name__ == '__main__':
    print(calculate_triangle_perimeter(3, 4, 5))
    print(calculate_triangle_perimeter(10, 10, 10))
    unittest.main()