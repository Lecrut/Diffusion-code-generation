import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(2), 4)

    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side(self):
        self.assertEqual(calculate_square_area(-3), 9)

if __name__ == '__main__':
    print(calculate_square_area(5))
    unittest.main(argv=[''], exit=False)