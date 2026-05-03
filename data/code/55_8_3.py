import unittest
def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Invalid triangle side lengths")
    return a + b + c
class TestPerimeterCalculation(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 12, 13), 30)
        self.assertEqual(calculate_perimeter(1, 1, 1), 3)
    def test_invalid_triangle_sides(self):
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(1, 2, 4)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(2, 3, 1)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(0, 4, 5)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(-1, 2, 3)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(1, 1, -1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)