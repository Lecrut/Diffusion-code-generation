import unittest

def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle side lengths")
    return a + b + c

class TestCalculatePerimeter(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(1, 1, 2)
        with self.assertRaises(ValueError):
            calculate_perimeter(7, 10, 5)

if __name__ == '__main__':
    try:
        print(calculate_perimeter(3, 4, 5))
    except ValueError as e:
        print(e)
    unittest.main(argv=[''], exit=False)