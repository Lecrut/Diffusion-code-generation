import unittest

def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side_length(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_length_exception(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-4)

    def test_non_numeric_side_length_exception(self):
        with self.assertRaises(TypeError):
            calculate_square_area("a")

if __name__ == '__main__':
    sample_values = [2, 5, -3, "a"]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side length {value}: {area}")
        except Exception as e:
            print(f"Error calculating area for side length {value}: {e}")