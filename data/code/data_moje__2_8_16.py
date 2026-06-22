import unittest
import math

def calculate_cylinder_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive.")
    return math.pi * (radius ** 2) * height

def calculate_sphere_volume(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return (4 / 3) * math.pi * (radius ** 3)

def calculate_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive.")
    return (1 / 3) * math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):

    def test_cylinder_positive_inputs(self):
        self.assertAlmostEqual(calculate_cylinder_volume(3, 5), 141.3716694115407)

    def test_cylinder_zero_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(0, 5)

    def test_cylinder_negative_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-3, 5)

    def test_cylinder_zero_height_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(3, 0)

    def test_cylinder_negative_height_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(3, -5)

    def test_cylinder_negative_both_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-3, -5)

    def test_sphere_positive_inputs(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), 113.09733552923255)

    def test_sphere_zero_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(0)

    def test_sphere_negative_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-3)

    def test_cone_positive_inputs(self):
        self.assertAlmostEqual(calculate_cone_volume(3, 5), 47.12388980384689)

    def test_cone_zero_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(0, 5)

    def test_cone_negative_radius_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-3, 5)

    def test_cone_zero_height_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(3, 0)

    def test_cone_negative_height_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(3, -5)

    def test_cone_negative_both_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-3, -5)

if __name__ == '__main__':
    res1 = calculate_cylinder_volume(1, 1)
    res2 = calculate_sphere_volume(1)
    res3 = calculate_cone_volume(1, 1)
    print(res1)
    print(res2)
    print(res3)
    unittest.main()