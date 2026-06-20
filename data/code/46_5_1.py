import math

def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle: sides do not satisfy the triangle inequality")
    return a + b + c

class TestTrianglePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)
        self.assertEqual(calculate_perimeter(6.0, 8.0, 10.0), 24.0)

    def test_invalid_triangle_inequality(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(1, 2, 10)
        with self.assertRaises(ValueError):
            calculate_perimeter(3, 3, 7)

    def test_non_positive_sides(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(0, 5, 5)
        with self.assertRaises(ValueError):
            calculate_perimeter(-1, 4, 5)
        with self.assertRaises(ValueError):
            calculate_perimeter(3, -2, 5)

if __name__ == '__main__':
    print(calculate_perimeter(3, 4, 5))
    print(calculate_perimeter(10, 10, 10))
    unittest.main()