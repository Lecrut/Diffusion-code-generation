import unittest

def calculate_square_area(side_length):
    if side_length < 0:
        return -1
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):

    def test_positive_side_length(self):
        self.assertEqual(calculate_square_area(3), 9)

    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_length(self):
        self.assertEqual(calculate_square_area(-4), -1)
if __name__ == '__main__':
    sample_values = [2, 5, -3]
    for value in sample_values:
        area = calculate_square_area(value)
        print(f'Area of square with side length {value}: {area}')
    unittest.main(argv=[''], exit=False)