import math
import unittest

class CircleAreaCalculator:
    @staticmethod
    def calculate_area(radius):
        return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_calculate_area(self):
        self.assertAlmostEqual(CircleAreaCalculator.calculate_area(1), math.pi)
        self.assertAlmostEqual(CircleAreaCalculator.calculate_area(0), 0)
        self.assertAlmostEqual(CircleAreaCalculator.calculate_area(2.5), math.pi * 6.25)

if __name__ == '__main__':
    print("Area of circle with radius 3:", CircleAreaCalculator.calculate_area(3))
    unittest.main(argv=[''], exit=False)