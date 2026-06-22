import unittest

def calculate_volume_cube(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

def calculate_volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    import math
    return (4/3) * math.pi * (radius ** 3)

class TestVolumeCalculations(unittest.TestCase):

    def test_calculate_volume_cube_positive(self):
        self.assertEqual(calculate_volume_cube(3), 27)
    
    def test_calculate_volume_cube_zero(self):
        self.assertEqual(calculate_volume_cube(0), 0)
    
    def test_calculate_volume_cube_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume_cube(-1)

    def test_calculate_volume_sphere_positive(self):
        import math
        expected = (4/3) * math.pi * (2 ** 3)
        self.assertAlmostEqual(calculate_volume_sphere(2), expected, places=5)
    
    def test_calculate_volume_sphere_zero(self):
        self.assertEqual(calculate_volume_sphere(0), 0)
    
    def test_calculate_volume_sphere_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume_sphere(-1)

if __name__ == '__main__':
    print("Volume of cube with side length 3:", calculate_volume_cube(3))
    print("Volume of sphere with radius 2:", calculate_volume_sphere(2))
    unittest.main(argv=[''], exit=False)