import unittest
import math

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return math.pi * (radius ** 2) * height

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4.0 / 3.0) * math.pi * (radius ** 3)

def calculate_cube_volume(side):
    if side < 0:
        raise ValueError("Side must be non-negative")
    return side ** 3

class TestCylinderVolume(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertAlmostEqual(calculate_cylinder_volume(1, 1), math.pi)
        self.assertAlmostEqual(calculate_cylinder_volume(2, 3), 12 * math.pi)

    def test_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(5, 0), 0)

    def test_zero_both(self):
        self.assertEqual(calculate_cylinder_volume(0, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(5, -1)

    def test_negative_both(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, -1)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_cylinder_volume(1.5, 2.5), math.pi * (1.5 ** 2) * 2.5)

class TestSphereVolume(unittest.TestCase):
    def test_normal_inputs(self):
        expected = (4.0 / 3.0) * math.pi * (1 ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(1), expected)
        expected = (4.0 / 3.0) * math.pi * (2 ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(2), expected)

    def test_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_float_inputs(self):
        expected = (4.0 / 3.0) * math.pi * (1.5 ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(1.5), expected)

class TestCubeVolume(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(calculate_cube_volume(1), 1)
        self.assertEqual(calculate_cube_volume(2), 8)
        self.assertEqual(calculate_cube_volume(3), 27)

    def test_zero_side(self):
        self.assertEqual(calculate_cube_volume(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-1)

    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_cube_volume(1.5), 1.5 ** 3)

if __name__ == '__main__':
    unittest.main()