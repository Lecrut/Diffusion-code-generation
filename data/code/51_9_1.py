import unittest
def calculate_perimeter(length, width):
    return 2 * (length + width)
class TestPerimeterCalculation(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_perimeter(5, 10), 30)
        self.assertEqual(calculate_perimeter(3, 4), 14)
        self.assertEqual(calculate_perimeter(1, 1), 4)
    def test_zero_input(self):
        self.assertEqual(calculate_perimeter(0, 5), 10)
        self.assertEqual(calculate_perimeter(0, 0), 0)
    def test_negative_inputs(self):
        self.assertEqual(calculate_perimeter(-5, 10), 10)
        self.assertEqual(calculate_perimeter(5, -10), -10)
        self.assertEqual(calculate_perimeter(-5, -10), -30)
    def test_mixed_signs(self):
        self.assertEqual(calculate_perimeter(10, -5), 10)
        self.assertEqual(calculate_perimeter(-10, 5), -10)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)