import unittest
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)
        self.assertAlmostEqual(calculate_circle_area(0.5), 0.7853981633974483)
        self.assertAlmostEqual(calculate_circle_area(2.5), 19.634954084936208)

if __name__ == '__main__':
    print("Area of circle with radius 1:", calculate_circle_area(1))
    print("Area of circle with radius 0.5:", calculate_circle_area(0.5))
    print("Area of circle with radius 2.5:", calculate_circle_area(2.5))
    unittest.main(argv=[''], exit=False)