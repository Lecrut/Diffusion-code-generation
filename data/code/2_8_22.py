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

    def test_calculate_volume_cube(self):
        self.assertEqual(calculate_volume_cube(0), 0)
        self.assertEqual(calculate_volume_cube(1), 1)
        self.assertEqual(calculate_volume_cube(-1), -1)
        self.assertEqual(calculate_volume_cube(2.5), 15.625)

    def test_calculate_volume_cylinder(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)
        self.assertEqual(calculate_volume_cylinder(5, 0), 0)
        self.assertEqual(calculate_volume_cylinder(-1, 5), -math.pi * 5)
        self.assertEqual(calculate_volume_cylinder(2, 3), 12 * math.pi)

    def test_calculate_volume_sphere(self):
        self.assertEqual(calculate_volume_sphere(0), 0)
        self.assertEqual(calculate_volume_sphere(1), (4/3) * math.pi)
        self.assertEqual(calculate_volume_sphere(-1), -(4/3) * math.pi)
        self.assertEqual(calculate_volume_sphere(2.5), (4/3) * math.pi * 15.625)

if __name__ == '__main__':
    print("Cube Volume:", calculate_volume_cube(3))
    print("Cylinder Volume:", calculate_volume_cylinder(2, 7))
    print("Sphere Volume:", calculate_volume_sphere(4))
    unittest.main(argv=[''], exit=False)