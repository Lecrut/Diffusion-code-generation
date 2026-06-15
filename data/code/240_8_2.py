import unittest
class TestSquareArea(unittest.TestCase):
    def calculate_square_area(self, side):
        return side * side
    def test_square_area_positive(self):
        self.assertEqual(self.calculate_square_area(5), 25)
        self.assertEqual(self.calculate_square_area(10), 100)
    def test_square_area_zero(self):
        self.assertEqual(self.calculate_square_area(0), 0)
    def test_square_area_float(self):
        self.assertAlmostEqual(self.calculate_square_area(2.5), 6.25)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)