import math
import unittest

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)
        self.assertAlmostEqual(calculate_circle_area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(calculate_circle_area(10), math.pi * 100)

    def test_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)

if __name__ == '__main__':
    print("Area of circle with radius 3:", calculate_circle_area(3))
    unittest.main(argv=[''], exit=False)