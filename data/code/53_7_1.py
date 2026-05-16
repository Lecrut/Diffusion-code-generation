import unittest
class TestSquareArea(unittest.TestCase):
    def test_area_positive_integer(self):
        self.assertEqual(calculate_square_area(4), 16)
    def test_area_zero(self):
        self.assertEqual(calculate_square_area(0), 0)
    def test_area_float(self):
        self.assertAlmostEqual(calculate_square_area(2.5), 6.25)
def calculate_square_area(side):
    return side * side
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)