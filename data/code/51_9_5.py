import unittest
def calculate_perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return 2 * (length + width)
class TestPerimeterCalculation(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_perimeter(5, 10), 30)
        self.assertEqual(calculate_perimeter(3, 7), 20)
        self.assertEqual(calculate_perimeter(1, 1), 4)
    def test_zero_input(self):
        self.assertEqual(calculate_perimeter(0, 5), 10)
        self.assertEqual(calculate_perimeter(10, 0), 20)
        self.assertEqual(calculate_perimeter(0, 0), 0)
    def test_mixed_inputs(self):
        self.assertEqual(calculate_perimeter(12, 4), 32)
        self.assertEqual(calculate_perimeter(1, 100), 202)
    def test_negative_input_raises_error(self):
        with self.assertRaisesRegex(ValueError, "Length and width must be non-negative"):
            calculate_perimeter(-5, 10)
        with self.assertRaisesRegex(ValueError, "Length and width must be non-negative"):
            calculate_perimeter(5, -10)
        with self.assertRaisesRegex(ValueError, "Length and width must be non-negative"):
            calculate_perimeter(-5, -10)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)