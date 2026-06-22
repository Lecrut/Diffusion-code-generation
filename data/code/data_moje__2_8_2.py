import unittest
import math

def calculate_volume_of_cube(side):
    if side <= 0:
        raise ValueError("Side length must be positive")
    return side ** 3

def calculate_volume_of_sphere(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return (4.0 / 3.0) * math.pi * (radius ** 3)

def calculate_volume_of_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive")
    return math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):
    def test_cube_positive(self):
        self.assertEqual(calculate_volume_of_cube(2), 8)
        self.assertEqual(calculate_volume_of_cube(3), 27)

    def test_cube_zero(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cube(0)

    def test_cube_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cube(-1)

    def test_sphere_positive(self):
        self.assertAlmostEqual(calculate_volume_of_sphere(1), (4.0 / 3.0) * math.pi)
        self.assertAlmostEqual(calculate_volume_of_sphere(3), 36 * math.pi)

    def test_sphere_zero(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_sphere(0)

    def test_sphere_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_sphere(-2)

    def test_cylinder_positive(self):
        self.assertAlmostEqual(calculate_volume_of_cylinder(1, 1), math.pi)
        self.assertAlmostEqual(calculate_volume_of_cylinder(2, 3), 12 * math.pi)

    def test_cylinder_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cylinder(0, 5)

    def test_cylinder_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cylinder(5, 0)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cylinder(-1, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_volume_of_cylinder(5, -1)

if __name__ == '__main__':
    print(calculate_volume_of_cube(3))
    print(calculate_volume_of_sphere(2))
    print(calculate_volume_of_cylinder(3, 4))
    unittest.main()