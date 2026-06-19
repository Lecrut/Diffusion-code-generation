import unittest
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_radius_0(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi, places=5)

    def test_radius_2(self):
        self.assertAlmostEqual(calculate_circle_area(2), 4 * math.pi, places=5)

    def test_radius_3(self):
        self.assertAlmostEqual(calculate_circle_area(3), 9 * math.pi, places=5)

    def test_radius_10(self):
        self.assertAlmostEqual(calculate_circle_area(10), 100 * math.pi, places=5)

if __name__ == '__main__':
    print("Area of circle with radius 5:", calculate_circle_area(5))
    unittest.main(argv=[''], exit=False)