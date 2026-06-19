import unittest

def calculate_volume_cube(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

def calculate_volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * 3.14159 * (radius ** 3)

def calculate_volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return 3.14159 * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube(self):
        self.assertEqual(calculate_volume_cube(0), 0)
        self.assertEqual(calculate_volume_cube(1), 1)
        self.assertEqual(calculate_volume_cube(3), 27)
        with self.assertRaises(ValueError):
            calculate_volume_cube(-1)

    def test_calculate_volume_sphere(self):
        self.assertEqual(calculate_volume_sphere(0), 0)
        self.assertAlmostEqual(calculate_volume_sphere(1), 4.18879, places=5)
        self.assertAlmostEqual(calculate_volume_sphere(2), 33.51032, places=5)
        with self.assertRaises(ValueError):
            calculate_volume_sphere(-1)

    def test_calculate_volume_cylinder(self):
        self.assertEqual(calculate_volume_cylinder(0, 5), 0)
        self.assertEqual(calculate_volume_cylinder(5, 0), 0)
        self.assertAlmostEqual(calculate_volume_cylinder(1, 1), 3.14159, places=5)
        self.assertAlmostEqual(calculate_volume_cylinder(2, 3), 37.69908, places=5)
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(-1, 3)
        with self.assertRaises(ValueError):
            calculate_volume_cylinder(1, -3)

if __name__ == '__main__':
    print(calculate_volume_cube(2))
    print(calculate_volume_sphere(2))
    print(calculate_volume_cylinder(2, 3))
    unittest.main(argv=[''], exit=False)