import unittest
class TestSquareArea(unittest.TestCase):
    def calculate_square_area(self, side):
        return side * side
    def test_square_area_positive(self):
        self.assertEqual(self.calculate_square_area(5), 25)
    def test_square_area_zero(self):
        self.assertEqual(self.calculate_square_area(0), 0)
    def test_square_area_large(self):
        self.assertEqual(self.calculate_square_area(100), 10000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)