import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(4), 16)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side(self):
        self.assertEqual(calculate_square_area(-3), 9)

if __name__ == '__main__':
    sample_values = [5, 7, -2]
    for value in sample_values:
        print(f"Area of square with side {value}: {calculate_square_area(value)}")
    unittest.main(argv=[''], exit=False)