import unittest
import math

def volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return math.pi * (radius ** 2) * height

def volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4/3) * math.pi * (radius ** 3)

def volume_cone(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return (1/3) * math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):
    def test_cylinder_positive_values(self):
        result = volume_cylinder(1, 1)
        expected = math.pi
        self.assertAlmostEqual(result, expected)

    def test_cylinder_zero_radius(self):
        result = volume_cylinder(0, 5)
        self.assertEqual(result, 0)

    def test_cylinder_zero_height(self):
        result = volume_cylinder(3, 0)
        self.assertEqual(result, 0)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cylinder(-1, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cylinder(1, -5)

    def test_cylinder_negative_both(self):
        with self.assertRaises(ValueError):
            volume_cylinder(-1, -5)

    def test_sphere_positive_value(self):
        result = volume_sphere(1)
        expected = (4/3) * math.pi
        self.assertAlmostEqual(result, expected)

    def test_sphere_zero_radius(self):
        result = volume_sphere(0)
        self.assertEqual(result, 0)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_cone_positive_values(self):
        result = volume_cone(1, 1)
        expected = math.pi / 3
        self.assertAlmostEqual(result, expected)

    def test_cone_zero_radius(self):
        result = volume_cone(0, 10)
        self.assertEqual(result, 0)

    def test_cone_zero_height(self):
        result = volume_cone(5, 0)
        self.assertEqual(result, 0)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cone(-1, 5)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cone(5, -5)

    def test_cone_negative_both(self):
        with self.assertRaises(ValueError):
            volume_cone(-1, -5)

if __name__ == '__main__':
    res_cyl = volume_cylinder(2, 3)
    res_sph = volume_sphere(3)
    res_cone = volume_cone(4, 5)
    print(res_cyl)
    print(res_sph)
    print(res_cone)
    unittest.main()