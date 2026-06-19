import math
from unittest import TestCase

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

class TestCircleArea(TestCase):
    def test_area_with_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)

    def test_area_with_radius_0(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_area_with_radius_2_5(self):
        self.assertAlmostEqual(calculate_circle_area(2.5), math.pi * (2.5 ** 2))

if __name__ == '__main__':
    print(calculate_circle_area(3))