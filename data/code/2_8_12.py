import unittest
import math

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * (radius ** 3)

def calculate_cube_volume(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 3

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):
    def test_sphere_volume_valid_radius(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), 113.09733552923255, places=5)

    def test_sphere_volume_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-5)

    def test_sphere_volume_float_radius(self):
        self.assertAlmostEqual(calculate_sphere_volume(2.5), 65.44984694978736, places=5)

    def test_cube_volume_valid_side(self):
        self.assertEqual(calculate_cube_volume(3), 27)

    def test_cube_volume_zero_side(self):
        self.assertEqual(calculate_cube_volume(0), 0)

    def test_cube_volume_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-4)

    def test_cube_volume_float_side(self):
        self.assertEqual(calculate_cube_volume(2.5), 15.625)

    def test_cylinder_volume_valid_inputs(self):
        self.assertAlmostEqual(calculate_cylinder_volume(3, 5), 141.3716694115407, places=5)

    def test_cylinder_volume_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_volume_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(3, 0), 0.0)

    def test_cylinder_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-3, 5)

    def test_cylinder_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(3, -5)

    def test_cylinder_volume_float_inputs(self):
        self.assertAlmostEqual(calculate_cylinder_volume(2.5, 4.0), 78.53981633974483, places=5)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    result_sphere = calculate_sphere_volume(3)
    result_cube = calculate_cube_volume(4)
    result_cylinder = calculate_cylinder_volume(2, 5)
    print(result_sphere)
    print(result_cube)
    print(result_cylinder)