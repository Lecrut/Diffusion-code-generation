import unittest
import math

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

    def test_sphere_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_positive_radius(self):
        result = calculate_sphere_volume(1)
        expected = (4.0 / 3.0) * math.pi
        self.assertAlmostEqual(result, expected, places=7)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_zero_dimensions(self):
        self.assertEqual(calculate_cylinder_volume(0, 10), 0.0)
        self.assertEqual(calculate_cylinder_volume(10, 0), 0.0)
        self.assertEqual(calculate_cylinder_volume(0, 0), 0.0)

    def test_cylinder_positive_dimensions(self):
        result = calculate_cylinder_volume(1, 1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=7)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 10)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(10, -1)

    def test_cone_zero_dimensions(self):
        self.assertEqual(calculate_cone_volume(0, 10), 0.0)
        self.assertEqual(calculate_cone_volume(10, 0), 0.0)
        self.assertEqual(calculate_cone_volume(0, 0), 0.0)

    def test_cone_positive_dimensions(self):
        result = calculate_cone_volume(1, 1)
        expected = math.pi / 3.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 10)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(10, -1)

if __name__ == '__main__':
    print(calculate_sphere_volume(3))
    print(calculate_cylinder_volume(3, 5))
    print(calculate_cone_volume(3, 5))
    unittest.main()