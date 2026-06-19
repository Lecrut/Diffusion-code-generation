import unittest
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_area_with_radius_0(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_area_with_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)

    def test_area_with_radius_2_5(self):
        self.assertAlmostEqual(calculate_circle_area(2.5), math.pi * 6.25)

    def test_area_with_radius_10(self):
        self.assertAlmostEqual(calculate_circle_area(10), math.pi * 100)

if __name__ == '__main__':
    print("Area of circle with radius 3:", calculate_circle_area(3))
    unittest.main(argv=[''], exit=False)