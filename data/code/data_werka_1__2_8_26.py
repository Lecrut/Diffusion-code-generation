import unittest

def calculate_volume_cube(side_length):
    return side_length ** 3

def calculate_volume_cylinder(radius, height):
    import math
    return math.pi * radius ** 2 * height

def calculate_volume_sphere(radius):
    import math
    return (4/3) * math.pi * radius ** 3

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube_positive(self):
        self.assertEqual(calculate_volume_cube(3), 27)

    def test_calculate_volume_cube_zero(self):
        self.assertEqual(calculate_volume_cube(0), 0)

    def test_calculate_volume_cube_negative(self):
        self.assertEqual(calculate_volume_cube(-3), -27)

    def test_calculate_volume_cylinder_positive(self):
        self.assertAlmostEqual(calculate_volume_cylinder(2, 5), 62.83185307179586)

    def test_calculate_volume_cylinder_zero_radius(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)

    def test_calculate_volume_cylinder_zero_height(self):
        self.assertEqual(calculate_volume_cylinder(2, 0), 0)

    def test_calculate_volume_cylinder_negative_radius(self):
        self.assertAlmostEqual(calculate_volume_cylinder(-2, 5), -62.83185307179586)

    def test_calculate_volume_cylinder_negative_height(self):
        self.assertAlmostEqual(calculate_volume_cylinder(2, -5), -62.83185307179586)

    def test_calculate_volume_sphere_positive(self):
        self.assertAlmostEqual(calculate_volume_sphere(3), 113.09733552923254)

    def test_calculate_volume_sphere_zero(self):
        self.assertEqual(calculate_volume_sphere(0), 0)

    def test_calculate_volume_sphere_negative(self):
        self.assertAlmostEqual(calculate_volume_sphere(-3), -113.09733552923254)

if __name__ == '__main__':
    print("Cube volume with side length 3:", calculate_volume_cube(3))
    print("Cylinder volume with radius 2 and height 5:", calculate_volume_cylinder(2, 5))
    print("Sphere volume with radius 3:", calculate_volume_sphere(3))