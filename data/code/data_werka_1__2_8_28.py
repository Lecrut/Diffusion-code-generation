import unittest

def calculate_volume_cube(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

def calculate_volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    import math
    return math.pi * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube_positive(self):
        self.assertEqual(calculate_volume_cube(3), 27)

    def test_calculate_volume_cube_zero(self):
        self.assertEqual(calculate_volume_cube(0), 0)

    def test_calculate_volume_cube_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume_cube(-1)

    def test_calculate_volume_cylinder_positive(self):
        self.assertAlmostEqual(calculate_volume_cylinder(2, 5), 62.83185307179586)

    def test_calculate_volume_cylinder_zero_radius(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)

    def test_calculate_volume_cylinder_zero_height(self):
        self.assertEqual(calculate_volume_cylinder(2, 0), 0)

    def test_calculate_volume_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(-1, 5)

    def test_calculate_volume_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(2, -1)

if __name__ == '__main__':
    print("Cube volume for side length 3:", calculate_volume_cube(3))
    print("Cylinder volume for radius 2 and height 5:", calculate_volume_cylinder(2, 5))
    unittest.main(argv=[''], exit=False)