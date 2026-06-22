import unittest
import math

PI = math.pi
FOUR_THIRDS = 4.0 / 3.0

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return PI * (radius ** 2) * height

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return FOUR_THIRDS * PI * (radius ** 3)

def calculate_cube_volume(side):
    if side < 0:
        raise ValueError("Side must be non-negative")
    return side ** 3

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return (1.0 / 3.0) * PI * (radius ** 2) * height

class TestVolumeCalculations(unittest.TestCase):
    def test_cylinder_positive(self):
        self.assertAlmostEqual(calculate_cylinder_volume(2, 5), PI * 4 * 5)
    
    def test_cylinder_zero(self):
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)
    
    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-2, 5)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(2, -5)

    def test_sphere_positive(self):
        self.assertAlmostEqual(calculate_sphere_volume(3), FOUR_THIRDS * PI * 27)
    
    def test_sphere_zero(self):
        self.assertEqual(calculate_sphere_volume(0), 0.0)
    
    def test_sphere_negative(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-3)

    def test_cube_positive(self):
        self.assertEqual(calculate_cube_volume(3), 27)
    
    def test_cube_zero(self):
        self.assertEqual(calculate_cube_volume(0), 0)
    
    def test_cube_negative(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-3)

    def test_cone_positive(self):
        self.assertAlmostEqual(calculate_cone_volume(2, 5), (1.0 / 3.0) * PI * 4 * 5)
    
    def test_cone_zero_height(self):
        self.assertEqual(calculate_cone_volume(2, 0), 0.0)
    
    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-2, 5)

if __name__ == '__main__':
    r = 5
    h = 10
    s = 4
    
    cylinder_res = calculate_cylinder_volume(r, h)
    print(cylinder_res)
    
    sphere_res = calculate_sphere_volume(r)
    print(sphere_res)
    
    cube_res = calculate_cube_volume(s)
    print(cube_res)
    
    cone_res = calculate_cone_volume(r, h)
    print(cone_res)
    
    unittest.main(exit=False)