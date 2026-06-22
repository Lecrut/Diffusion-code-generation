import unittest
import math

def calculate_cube_volume(side: float) -> float:
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return side ** 3

def calculate_sphere_volume(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4 / 3) * math.pi * (radius ** 3)

def calculate_cylinder_volume(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return math.pi * (radius ** 2) * height

def calculate_cone_volume(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return (1 / 3) * math.pi * (radius ** 2) * height

class TestVolumeFunctions(unittest.TestCase):

    def test_cube_volume_positive(self):
        self.assertAlmostEqual(calculate_cube_volume(2), 8)

    def test_cube_volume_zero(self):
        self.assertAlmostEqual(calculate_cube_volume(0), 0)

    def test_cube_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-1)

    def test_sphere_volume_positive(self):
        expected = (4 / 3) * math.pi * (2 ** 3)
        self.assertAlmostEqual(calculate_sphere_volume(2), expected)

    def test_sphere_volume_zero(self):
        self.assertAlmostEqual(calculate_sphere_volume(0), 0)

    def test_sphere_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_volume_positive(self):
        expected = math.pi * (1 ** 2) * 5
        self.assertAlmostEqual(calculate_cylinder_volume(1, 5), expected)

    def test_cylinder_volume_zero_radius(self):
        self.assertAlmostEqual(calculate_cylinder_volume(0, 5), 0)

    def test_cylinder_volume_zero_height(self):
        self.assertAlmostEqual(calculate_cylinder_volume(1, 0), 0)

    def test_cylinder_volume_zero_both(self):
        self.assertAlmostEqual(calculate_cylinder_volume(0, 0), 0)

    def test_cylinder_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(1, -5)

    def test_cone_volume_positive(self):
        expected = (1 / 3) * math.pi * (1 ** 2) * 5
        self.assertAlmostEqual(calculate_cone_volume(1, 5), expected)

    def test_cone_volume_zero_radius(self):
        self.assertAlmostEqual(calculate_cone_volume(0, 5), 0)

    def test_cone_volume_zero_height(self):
        self.assertAlmostEqual(calculate_cone_volume(1, 0), 0)

    def test_cone_volume_zero_both(self):
        self.assertAlmostEqual(calculate_cone_volume(0, 0), 0)

    def test_cone_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)

    def test_cone_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(1, -5)

if __name__ == '__main__':
    cube_res = calculate_cube_volume(3)
    sphere_res = calculate_sphere_volume(2)
    cylinder_res = calculate_cylinder_volume(3, 5)
    cone_res = calculate_cone_volume(3, 5)

    print(cube_res)
    print(sphere_res)
    print(cylinder_res)
    print(cone_res)

    unittest.main()