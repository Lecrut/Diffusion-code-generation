import unittest
import math

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if radius == 0:
        return 0.0
    return (4.0 / 3.0) * math.pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    if radius == 0 or height == 0:
        return 0.0
    return math.pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    if radius == 0 or height == 0:
        return 0.0
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):

    def test_sphere_positive_radius(self):
        result = calculate_sphere_volume(1)
        self.assertAlmostEqual(result, 4.1887902047863905)

    def test_sphere_zero_radius(self):
        result = calculate_sphere_volume(0)
        self.assertEqual(result, 0.0)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_positive_values(self):
        result = calculate_cylinder_volume(1, 1)
        self.assertAlmostEqual(result, 3.141592653589793)

    def test_cylinder_zero_radius(self):
        result = calculate_cylinder_volume(0, 5)
        self.assertEqual(result, 0.0)

    def test_cylinder_zero_height(self):
        result = calculate_cylinder_volume(5, 0)
        self.assertEqual(result, 0.0)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(5, -1)

    def test_cone_positive_values(self):
        result = calculate_cone_volume(1, 3)
        self.assertAlmostEqual(result, 3.141592653589793)

    def test_cone_zero_radius(self):
        result = calculate_cone_volume(0, 5)
        self.assertEqual(result, 0.0)

    def test_cone_zero_height(self):
        result = calculate_cone_volume(5, 0)
        self.assertEqual(result, 0.0)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(5, -1)

if __name__ == '__main__':
    sphere_vol = calculate_sphere_volume(2)
    cylinder_vol = calculate_cylinder_volume(3, 4)
    cone_vol = calculate_cone_volume(3, 4)
    print(f"Sphere Volume: {sphere_vol}")
    print(f"Cylinder Volume: {cylinder_vol}")
    print(f"Cone Volume: {cone_vol}")
    unittest.main()