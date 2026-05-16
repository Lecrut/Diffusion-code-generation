import unittest
class TestSquareArea(unittest.TestCase):
    def test_square_area_positive(self):
        self.assertEqual(calculate_square_area(4), 16)
        self.assertEqual(calculate_square_area(10.5), 110.25)
    def test_square_area_zero(self):
        self.assertEqual(calculate_square_area(0), 0)
    def test_square_area_negative(self):
        self.assertEqual(calculate_square_area(-5), 25)
def calculate_square_area(side):
    return side * side
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)