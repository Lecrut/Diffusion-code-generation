import unittest
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_area_with_radius_0(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_area_with_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)

    def test_area_with_radius_2(self):
        self.assertAlmostEqual(calculate_circle_area(2), 4 * math.pi)

    def test_area_with_radius_3(self):
        self.assertAlmostEqual(calculate_circle_area(3), 9 * math.pi)

if __name__ == '__main__':
    print("Area of circle with radius 0:", calculate_circle_area(0))
    print("Area of circle with radius 1:", calculate_circle_area(1))
    print("Area of circle with radius 2:", calculate_circle_area(2))
    print("Area of circle with radius 3:", calculate_circle_area(3))
    unittest.main(argv=[''], exit=False)