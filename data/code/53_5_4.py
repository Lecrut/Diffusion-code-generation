import unittest

def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side_length(self):
        self.assertEqual(calculate_square_area(4), 16)

    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_length_exception(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

if __name__ == '__main__':
    sample_values = [2, 5, -3]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side length {value}: {area}")
        except ValueError as e:
            print(f"Error calculating area for side length {value}: {e}")

    unittest.main(argv=[''], exit=False)