import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(4), 16)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side(self):
        self.assertEqual(calculate_square_area(-3), 9)

if __name__ == '__main__':
    side_length = 5
    area = calculate_square_area(side_length)
    print(f"The area of a square with side length {side_length} is {area}")
    unittest.main(argv=[''], exit=False)