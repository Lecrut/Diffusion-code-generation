import unittest

def calculate_volume_cube(side_length):
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return side_length ** 3

def calculate_volume_sphere(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    import math
    return 4 / 3 * math.pi * radius ** 3

def calculate_volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError('Radius and height cannot be negative')
    import math
    return math.pi * radius ** 2 * height

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube(self):
        self.assertEqual(calculate_volume_cube(0), 0)
        self.assertEqual(calculate_volume_cube(1), 1)
        self.assertEqual(calculate_volume_cube(3), 27)
        with self.assertRaises(ValueError):
            calculate_volume_cube(-1)

    def test_calculate_volume_sphere(self):
        self.assertEqual(calculate_volume_sphere(0), 0)
        self.assertAlmostEqual(calculate_volume_sphere(1), 4.1887902047863905, places=9)
        self.assertAlmostEqual(calculate_volume_sphere(2), 33.510321638291124, places=9)
        with self.assertRaises(ValueError):
            calculate_volume_sphere(-1)

    def test_calculate_volume_cylinder(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)
        self.assertEqual(calculate_volume_cylinder(5, 0), 0)
        self.assertAlmostEqual(calculate_volume_cylinder(1, 2), 6.283185307179586, places=9)
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(-1, 2)
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(1, -2)
if __name__ == '__main__':
    print(calculate_volume_cube(3))
    print(calculate_volume_sphere(2))
    print(calculate_volume_cylinder(1, 2))
    unittest.main(argv=[''], exit=False)