import unittest
import math

def calculate_volume_cube(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 3

def calculate_volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * radius ** 3

def calculate_volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return math.pi * radius ** 2 * height

class TestVolumeCalculations(unittest.TestCase):
    def test_cube_positive(self):
        self.assertAlmostEqual(calculate_volume_cube(3), 27.0)

    def test_cube_zero(self):
        self.assertEqual(calculate_volume_cube(0), 0)

    def test_cube_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_volume_cube(-1)

    def test_sphere_positive(self):
        expected = (4/3) * math.pi * 1 ** 3
        self.assertAlmostEqual(calculate_volume_sphere(1), expected)

    def test_sphere_zero(self):
        self.assertAlmostEqual(calculate_volume_sphere(0), 0.0)

    def test_sphere_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_volume_sphere(-1)

    def test_cylinder_positive(self):
        expected = math.pi * 1 ** 2 * 1
        self.assertAlmostEqual(calculate_volume_cylinder(1, 1), expected)

    def test_cylinder_zero_radius(self):
        self.assertAlmostEqual(calculate_volume_cylinder(0, 1), 0.0)

    def test_cylinder_zero_height(self):
        self.assertAlmostEqual(calculate_volume_cylinder(1, 0), 0.0)

    def test_cylinder_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(-1, 1)

    def test_cylinder_negative_height_raises(self):
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(1, -1)

    def test_cube_float(self):
        self.assertAlmostEqual(calculate_volume_cube(2.5), 15.625)

    def test_sphere_float(self):
        expected = (4/3) * math.pi * 2.5 ** 3
        self.assertAlmostEqual(calculate_volume_sphere(2.5), expected)

    def test_cylinder_float(self):
        expected = math.pi * 2.5 ** 2 * 3.5
        self.assertAlmostEqual(calculate_volume_cylinder(2.5, 3.5), expected)

if __name__ == '__main__':
    print(calculate_volume_cube(3))
    print(calculate_volume_sphere(1))
    print(calculate_volume_cylinder(1, 2))
    unittest.main(argv=[''], exit=False)