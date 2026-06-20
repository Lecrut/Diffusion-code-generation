def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if radius == 0:
        return 0.0
    return (4.0 / 3.0) * 3.141592653589793 * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    if radius == 0 or height == 0:
        return 0.0
    return 3.141592653589793 * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    if radius == 0 or height == 0:
        return 0.0
    return (1.0 / 3.0) * 3.141592653589793 * (radius ** 2) * height

import unittest

class TestVolumeCalculations(unittest.TestCase):
    def test_sphere_positive_radius(self):
        self.assertAlmostEqual(calculate_sphere_volume(1), 4.1887902047863905)
        self.assertAlmostEqual(calculate_sphere_volume(5), 523.5987755982989)

    def test_sphere_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_positive_radius_height(self):
        self.assertAlmostEqual(calculate_cylinder_volume(1, 1), 3.141592653589793)
        self.assertAlmostEqual(calculate_cylinder_volume(3, 5), 141.3716694115407)

    def test_cylinder_zero_radius(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_zero_height(self):
        self.assertEqual(calculate_cylinder_volume(3, 0), 0.0)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-2, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(2, -5)

    def test_cone_positive_radius_height(self):
        self.assertAlmostEqual(calculate_cone_volume(1, 1), 1.0471975511965976)
        self.assertAlmostEqual(calculate_cone_volume(3, 5), 47.1238898038469)

    def test_cone_zero_radius(self):
        self.assertEqual(calculate_cone_volume(0, 5), 0.0)

    def test_cone_zero_height(self):
        self.assertEqual(calculate_cone_volume(3, 0), 0.0)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-2, 5)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(2, -5)

if __name__ == '__main__':
    print(calculate_sphere_volume(2))
    print(calculate_cylinder_volume(2, 4))
    print(calculate_cone_volume(2, 4))
    unittest.main()