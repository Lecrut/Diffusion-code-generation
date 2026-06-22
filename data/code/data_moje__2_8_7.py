import math
import unittest

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4.0 / 3.0) * math.pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return math.pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):
    def test_sphere_volume_positive(self):
        self.assertAlmostEqual(calculate_sphere_volume(1), 4.1887902047863905)
        self.assertAlmostEqual(calculate_sphere_volume(2), 33.510321638291124)

    def test_sphere_volume_zero(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_volume_positive(self):
        self.assertAlmostEqual(calculate_cylinder_volume(1, 1), 3.141592653589793)
        self.assertAlmostEqual(calculate_cylinder_volume(2, 5), 62.83185307179586)

    def test_cylinder_volume_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_volume_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(1, 0), 0.0)

    def test_cylinder_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(1, -5)

    def test_cone_volume_positive(self):
        self.assertAlmostEqual(calculate_cone_volume(1, 1), 1.0471975511965976)
        self.assertAlmostEqual(calculate_cone_volume(2, 3), 12.566370614359172)

    def test_cone_volume_zero_radius(self):
        self.assertEqual(calculate_cone_volume(0, 5), 0.0)

    def test_cone_volume_zero_height(self):
        self.assertEqual(calculate_cone_volume(1, 0), 0.0)

    def test_cone_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)

    def test_cone_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(1, -5)

if __name__ == '__main__':
    print(calculate_sphere_volume(1))
    print(calculate_cylinder_volume(2, 3))
    print(calculate_cone_volume(3, 4))
    unittest.main(verbosity=0)