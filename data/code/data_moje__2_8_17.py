import math

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    if radius == 0 or height == 0:
        return 0.0
    return math.pi * radius * radius * height

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    if radius == 0:
        return 0.0
    return (4.0 / 3.0) * math.pi * radius * radius * radius

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    if radius == 0 or height == 0:
        return 0.0
    return (1.0 / 3.0) * math.pi * radius * radius * height

import unittest

class TestVolumeCalculations(unittest.TestCase):
    def test_cylinder_positive_values(self):
        self.assertAlmostEqual(calculate_cylinder_volume(2, 3), 37.69911184307752, places=5)

    def test_cylinder_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(3, 0), 0.0)

    def test_cylinder_both_zero(self):
        self.assertEqual(calculate_cylinder_volume(0, 0), 0.0)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(1, -5)

    def test_sphere_positive_value(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), 113.09733552923254, places=5)

    def test_sphere_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cone_positive_values(self):
        self.assertAlmostEqual(calculate_cone_volume(3, 3), 28.274333882308138, places=5)

    def test_cone_zero_radius(self):
        self.assertEqual(calculate_cone_volume(0, 5), 0.0)

    def test_cone_zero_height(self):
        self.assertEqual(calculate_cone_volume(3, 0), 0.0)

    def test_cone_both_zero(self):
        self.assertEqual(calculate_cone_volume(0, 0), 0.0)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(1, -5)

if __name__ == '__main__':
    print(calculate_cylinder_volume(2, 3))
    print(calculate_cylinder_volume(0, 5))
    print(calculate_cylinder_volume(3, 0))
    print(calculate_sphere_volume(3))
    print(calculate_sphere_volume(0))
    print(calculate_cone_volume(3, 3))
    print(calculate_cone_volume(0, 5))
    print(calculate_cone_volume(3, 0))
    unittest.main()