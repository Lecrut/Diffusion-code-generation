import unittest

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle")
    return a + b + c

class TestTrianglePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_triangle_perimeter(5, 5, 5), 15)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(-1, 4, 5)
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(3, 0, 5)
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(3, 4, 0)

    def test_non_triangle(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(1, 2, 3)
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(7, 10, 5)

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
    except ValueError as e:
        print(e)
    unittest.main(argv=[''], exit=False)