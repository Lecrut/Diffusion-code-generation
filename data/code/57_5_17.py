import math
import unittest

class CircleCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return CircleCalculator.PI * (radius ** 2)

class TestCircleCalculator(unittest.TestCase):
    def test_calculate_area(self):
        self.assertAlmostEqual(CircleCalculator.calculate_area(1), math.pi)
        self.assertAlmostEqual(CircleCalculator.calculate_area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(CircleCalculator.calculate_area(0), 0)
        with self.assertRaises(ValueError):
            CircleCalculator.calculate_area(-3)

if __name__ == '__main__':
    print(CircleCalculator.calculate_area(1))
    print(CircleCalculator.calculate_area(2.5))
    print(CircleCalculator.calculate_area(0))