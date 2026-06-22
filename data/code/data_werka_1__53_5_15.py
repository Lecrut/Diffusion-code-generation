import unittest

def calculate_square_area(side_length):
    return side_length * side_length

class TestCalculateSquareArea(unittest.TestCase):
    def test_positive_side_length(self):
        self.assertEqual(calculate_square_area(3), 9)
    
    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)
    
    def test_negative_side_length(self):
        self.assertEqual(calculate_square_area(-4), 16)

if __name__ == '__main__':
    side_lengths = [7, 0, -2]
    for length in side_lengths:
        area_result = calculate_square_area(length)
        print(f"The area of a square with side length {length} is {area_result}")