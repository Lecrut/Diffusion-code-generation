import unittest
import math

def calculate_volume(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return length * width * height

def calculate_sphere_volume(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return (4.0 / 3.0) * math.pi * (radius ** 3)

class TestVolumeCalculations(unittest.TestCase):
    def test_normal_cuboid_volume(self):
        result = calculate_volume(2, 3, 4)
        self.assertEqual(result, 24)

    def test_zero_length_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(0, 3, 4)

    def test_negative_length_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, 3, 4)

    def test_zero_width_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(2, 0, 4)

    def test_negative_width_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(2, -1, 4)

    def test_zero_height_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(2, 3, 0)

    def test_negative_height_cuboid(self):
        with self.assertRaises(ValueError):
            calculate_volume(2, 3, -1)

    def test_normal_sphere_volume(self):
        result = calculate_sphere_volume(3)
        expected = (4.0 / 3.0) * math.pi * 27
        self.assertAlmostEqual(result, expected)

    def test_zero_radius_sphere(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(0)

    def test_negative_radius_sphere(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

if __name__ == '__main__':
    print(calculate_volume(5, 10, 2))
    try:
        calculate_volume(0, 5, 5)
    except ValueError as e:
        print(e)
    try:
        calculate_sphere_volume(-5)
    except ValueError as e:
        print(e)
    print(calculate_sphere_volume(1))
    unittest.main()