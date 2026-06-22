import unittest

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    return a + b + c

class TestTrianglePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_triangle_perimeter(3, 4, 5), 12)
    
    def test_equilateral_triangle(self):
        self.assertEqual(calculate_triangle_perimeter(5, 5, 5), 15)
    
    def test_isosceles_triangle(self):
        self.assertEqual(calculate_triangle_perimeter(5, 5, 8), 18)
    
    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(0, 4, 5)
    
    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(-3, 4, 5)
    
    def test_invalid_triangle_not_a_triangle(self):
        with self.assertRaises(ValueError):
            calculate_triangle_perimeter(1, 2, 3)

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
    except ValueError as e:
        print(e)