import unittest

def calculate_perimeter(a: float, b: float, c: float) -> float:
    if not all((isinstance(side, (int, float)) for side in [a, b, c])):
        raise TypeError('All sides must be numbers')
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid triangle side lengths')
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

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_perimeter('a', 4, 5)
if __name__ == '__main__':
    try:
        side_a = 3.0
        side_b = 4.0
        side_c = 5.0
        perimeter = calculate_perimeter(side_a, side_b, side_c)
        print(f'The perimeter of the triangle is: {perimeter}')
    except Exception as e:
        print(f'Error: {e}')
    unittest.main(argv=[''], exit=False)