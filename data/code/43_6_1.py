import unittest
class SquareCalculator:
    def calculate_area(self, side):
        return side * side
class TestSquareCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SquareCalculator()
    def test_area_positive_integer(self):
        result = self.calculator.calculate_area(5)
        self.assertEqual(result, 25)
    def test_area_zero(self):
        result = self.calculator.calculate_area(0)
        self.assertEqual(result, 0)
    def test_area_float(self):
        result = self.calculator.calculate_area(2.5)
        self.assertEqual(result, 6.25)
    def test_area_large_number(self):
        result = self.calculator.calculate_area(100)
        self.assertEqual(result, 10000)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)