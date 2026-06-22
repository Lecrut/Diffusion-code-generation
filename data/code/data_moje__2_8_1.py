import unittest
import math

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    if radius == 0 or height == 0:
        return 0.0
    return math.pi * (radius ** 2) * height

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4 / 3) * math.pi * (radius ** 3)

def calculate_cuboid_volume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return length * width * height

class TestVolumeCalculations(unittest.TestCase):

    def test_cylinder_volume_positive(self):
        self.assertAlmostEqual(calculate_cylinder_volume(3, 5), 141.3716694115407, places=5)

    def test_cylinder_volume_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_volume_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(3, 0), 0.0)

    def test_cylinder_volume_both_zero(self):
        self.assertEqual(calculate_cylinder_volume(0, 0), 0.0)

    def test_cylinder_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-3, 5)

    def test_cylinder_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(3, -5)

    def test_sphere_volume_positive(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), 113.09733552923255, places=5)

    def test_sphere_volume_zero(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-3)

    def test_cuboid_volume_positive(self):
        self.assertEqual(calculate_cuboid_volume(2, 3, 4), 24)

    def test_cuboid_volume_zero_length(self):
        self.assertEqual(calculate_cuboid_volume(0, 3, 4), 0)

    def test_cuboid_volume_zero_width(self):
        self.assertEqual(calculate_cuboid_volume(2, 0, 4), 0)

    def test_cuboid_volume_zero_height(self):
        self.assertEqual(calculate_cuboid_volume(2, 3, 0), 0)

    def test_cuboid_volume_all_zero(self):
        self.assertEqual(calculate_cuboid_volume(0, 0, 0), 0)

    def test_cuboid_volume_negative_length(self):
        with self.assertRaises(ValueError):
            calculate_cuboid_volume(-2, 3, 4)

    def test_cuboid_volume_negative_width(self):
        with self.assertRaises(ValueError):
            calculate_cuboid_volume(2, -3, 4)

    def test_cuboid_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cuboid_volume(2, 3, -4)

def run_main():
    r = 5
    h = 10
    vol_cyl = calculate_cylinder_volume(r, h)
    vol_sphere = calculate_sphere_volume(r)
    l, w, d = 2, 3, 4
    vol_cuboid = calculate_cuboid_volume(l, w, d)
    print(vol_cyl)
    print(vol_sphere)
    print(vol_cuboid)

if __name__ == '__main__':
    run_main()
    unittest.main()