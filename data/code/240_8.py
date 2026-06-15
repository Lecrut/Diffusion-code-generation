import unittest
class TestSquareArea(unittest.TestCase):
    def calculate_square_area(self, side):
        return side * side
    def test_area_of_positive_number(self):
        self.assertEqual(self.calculate_square_area(5), 25)
    def test_area_of_zero(self):
        self.assertEqual(self.calculate_square_area(0), 0)
    def test_area_of_large_number(self):
        self.assertEqual(self.calculate_square_area(100), 10000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)