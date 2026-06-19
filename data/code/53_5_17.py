import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side_length(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_length(self):
        self.assertEqual(calculate_square_area(-3), 9)

if __name__ == '__main__':
    print("Area of square with side length 4:", calculate_square_area(4))
    unittest.main(argv=[''], exit=False)