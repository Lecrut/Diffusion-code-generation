import unittest

def calculate_volume_cube(side_length):
    return side_length ** 3

def calculate_volume_sphere(radius):
    import math
    return (4/3) * math.pi * radius ** 3

def calculate_volume_cylinder(radius, height):
    import math
    return math.pi * radius ** 2 * height

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube(self):
        self.assertEqual(calculate_volume_cube(0), 0)
        self.assertEqual(calculate_volume_cube(1), 1)
        self.assertEqual(calculate_volume_cube(-1), -1)
        self.assertEqual(calculate_volume_cube(2.5), 15.625)

    def test_calculate_volume_sphere(self):
        self.assertEqual(calculate_volume_sphere(0), 0)
        self.assertEqual(calculate_volume_sphere(1), (4/3) * 3.141592653589793)
        self.assertEqual(calculate_volume_sphere(-1), (-4/3) * 3.141592653589793)
        self.assertEqual(calculate_volume_sphere(2.5), (4/3) * 3.141592653589793 * 15.625)

    def test_calculate_volume_cylinder(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)
        self.assertEqual(calculate_volume_cylinder(5, 0), 0)
        self.assertEqual(calculate_volume_cylinder(-1, 5), -3.141592653589793 * 5)
        self.assertEqual(calculate_volume_cylinder(1, -5), -3.141592653589793 * 1)
        self.assertEqual(calculate_volume_cylinder(2.5, 5), 3.141592653589793 * 15.625)

if __name__ == '__main__':
    print("Cube volume with side length 3:", calculate_volume_cube(3))
    print("Sphere volume with radius 3:", calculate_volume_sphere(3))
    print("Cylinder volume with radius 3 and height 5:", calculate_volume_cylinder(3, 5))
    unittest.main(argv=[''], exit=False)