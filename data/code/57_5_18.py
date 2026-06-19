import unittest
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    
    def test_area_with_radius_0(self):
        self.assertEqual(calculate_circle_area(0), 0.0)
    
    def test_area_with_radius_1(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi, places=5)
    
    def test_area_with_radius_2_5(self):
        self.assertAlmostEqual(calculate_circle_area(2.5), 19.63495, places=5)
    
    def test_area_with_radius_10(self):
        self.assertAlmostEqual(calculate_circle_area(10), 314.15927, places=5)

if __name__ == '__main__':
    sample_radii = [0, 1, 2.5, 10]
    for radius in sample_radii:
        print(f"Area of circle with radius {radius}: {calculate_circle_area(radius)}")