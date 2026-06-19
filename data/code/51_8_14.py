import unittest

def calculate_perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError('Length and width must be non-negative')
    return 2 * (length + width)

class TestPerimeterCalculation(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_perimeter(5, 3), 16)

    def test_zero_length(self):
        self.assertEqual(calculate_perimeter(0, 3), 6)

    def test_zero_width(self):
        self.assertEqual(calculate_perimeter(5, 0), 10)

    def test_zero_values(self):
        self.assertEqual(calculate_perimeter(0, 0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(-5, 3)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(5, -3)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(-5, -3)
if __name__ == '__main__':
    print(calculate_perimeter(10, 5))
    print(calculate_perimeter(0, 0))
    print(calculate_perimeter(7, -2))
    unittest.main(argv=[''], exit=False)