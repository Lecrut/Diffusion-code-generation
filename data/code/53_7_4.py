import unittest
class TestSquareArea(unittest.TestCase):
    def test_area_positive_side(self):
        self.assertEqual(calculate_square_area(5), 25)
    def test_area_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)
    def test_area_large_side(self):
        self.assertEqual(calculate_square_area(100), 10000)
def calculate_square_area(side):
    return side * side
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)