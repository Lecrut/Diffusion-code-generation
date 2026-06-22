import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side(self):
        self.assertEqual(calculate_square_area(-4), 16)

if __name__ == '__main__':
    sample_values = [1, 7, -2]
    for value in sample_values:
        print(f"Area of square with side length {value}: {calculate_square_area(value)}")