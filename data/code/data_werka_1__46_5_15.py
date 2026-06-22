import unittest

def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    return a + b + c

class TestCalculatePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
    
    def test_equilateral_triangle(self):
        self.assertEqual(calculate_perimeter(7, 7, 7), 21)
    
    def test_isosceles_triangle(self):
        self.assertEqual(calculate_perimeter(6, 6, 8), 20)
    
    def test_invalid_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(0, 5, 5)
    
    def test_invalid_triangle_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(-1, 4, 5)

if __name__ == '__main__':
    side_a = 2
    side_b = 3
    side_c = 4
    try:
        perimeter = calculate_perimeter(side_a, side_b, side_c)
        print(f"The perimeter of the triangle is: {perimeter}")
    except ValueError as e:
        print(e)