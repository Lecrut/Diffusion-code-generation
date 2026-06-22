import unittest

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.141592653589793
    return (4.0 / 3.0) * pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    pi = 3.141592653589793
    return pi * (radius ** 2) * height

class TestVolumeFunctions(unittest.TestCase):

    def test_sphere_radius_zero(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_radius_positive(self):
        result = calculate_sphere_volume(1)
        expected = 4.1887902047863905
        self.assertAlmostEqual(result, expected, places=7)

    def test_sphere_radius_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-5)

    def test_cylinder_radius_zero(self):
        self.assertEqual(calculate_cylinder_volume(0, 10), 0.0)

    def test_cylinder_height_zero(self):
        self.assertEqual(calculate_cylinder_volume(5, 0), 0.0)

    def test_cylinder_radius_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-5, 10)

    def test_cylinder_height_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(5, -10)

    def test_cylinder_valid_values(self):
        result = calculate_cylinder_volume(1, 1)
        expected = 3.141592653589793
        self.assertAlmostEqual(result, expected, places=7)

if __name__ == '__main__':
    sphere_result = calculate_sphere_volume(2)
    print(sphere_result)
    cylinder_result = calculate_cylinder_volume(3, 4)
    print(cylinder_result)
    unittest.main()