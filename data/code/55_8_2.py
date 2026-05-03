import unittest
def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Invalid triangle side lengths")
    return a + b + c
class TestPerimeterCalculation(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)
        self.assertEqual(calculate_perimeter(10, 20, 30), 60)
    def test_invalid_triangle_side_lengths(self):
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(1, 2, 4)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(1, 1, 10)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(-1, 2, 3)
        with self.assertRaisesRegex(ValueError, "Invalid triangle side lengths"):
            calculate_perimeter(0, 5, 5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)