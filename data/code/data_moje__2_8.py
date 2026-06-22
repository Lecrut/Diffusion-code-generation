import unittest

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * 3.141592653589793 * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 3.141592653589793 * (radius ** 2) * height

def calculate_cube_volume(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 3

class TestVolumeCalculations(unittest.TestCase):

    def test_sphere_zero_radius(self):
        self.assertEqual(calculate_sphere_volume(0), 0)

    def test_sphere_positive_radius(self):
        expected = (4/3) * 3.141592653589793 * (5 ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(5), expected)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_zero_dimensions(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0)
        self.assertEqual(calculate_cylinder_volume(5, 0), 0)
        self.assertEqual(calculate_cylinder_volume(0, 0), 0)

    def test_cylinder_positive_dimensions(self):
        expected = 3.141592653589793 * (3 ** 2) * 10
        self.assertAlmostEqual(calculate_cylinder_volume(3, 10), expected)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(5, -1)

    def test_cube_zero_side(self):
        self.assertEqual(calculate_cube_volume(0), 0)

    def test_cube_positive_side(self):
        self.assertEqual(calculate_cube_volume(4), 64)

    def test_cube_negative_side(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-2)

if __name__ == '__main__':
    unittest.main()
    print(calculate_sphere_volume(5))
    print(calculate_cylinder_volume(3, 10))
    print(calculate_cube_volume(4))