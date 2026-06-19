import unittest

def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid triangle side lengths')
    return a + b + c

class TestCalculatePerimeter(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)
        self.assertEqual(calculate_perimeter(7, 10, 5), 22)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(1, 1, 2)
        with self.assertRaises(ValueError):
            calculate_perimeter(-1, 4, 5)
        with self.assertRaises(ValueError):
            calculate_perimeter(0, 4, 5)
if __name__ == '__main__':
    print(calculate_perimeter(3, 4, 5))
    unittest.main(argv=[''], exit=False)