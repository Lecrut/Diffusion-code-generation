import unittest

def calculate_cube_volume(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 3

def calculate_sphere_volume(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * 3.141592653589793 * radius ** 3

def calculate_cylinder_volume(radius, height):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 3.141592653589793 * radius ** 2 * height

def calculate_cone_volume(radius, height):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return (1/3) * 3.141592653589793 * radius ** 2 * height

class TestVolumeCalculations(unittest.TestCase):
    def test_cube_volume_positive(self):
        self.assertAlmostEqual(calculate_cube_volume(3), 27.0)

    def test_cube_volume_zero(self):
        self.assertAlmostEqual(calculate_cube_volume(0), 0.0)

    def test_cube_volume_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_cube_volume(-1)

    def test_cube_volume_non_number_raises(self):
        with self.assertRaises(TypeError):
            calculate_cube_volume("3")

    def test_sphere_volume_positive(self):
        expected = (4/3) * 3.141592653589793 * 3 ** 3
        self.assertAlmostEqual(calculate_sphere_volume(3), expected)

    def test_sphere_volume_zero(self):
        self.assertAlmostEqual(calculate_sphere_volume(0), 0.0)

    def test_sphere_volume_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_sphere_volume_non_number_raises(self):
        with self.assertRaises(TypeError):
            calculate_sphere_volume("3")

    def test_cylinder_volume_positive(self):
        expected = 3.141592653589793 * 2 ** 2 * 5
        self.assertAlmostEqual(calculate_cylinder_volume(2, 5), expected)

    def test_cylinder_volume_zero_radius(self):
        self.assertAlmostEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_volume_zero_height(self):
        self.assertAlmostEqual(calculate_cylinder_volume(2, 0), 0.0)

    def test_cylinder_volume_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)

    def test_cylinder_volume_negative_height_raises(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(2, -5)

    def test_cylinder_volume_non_number_radius_raises(self):
        with self.assertRaises(TypeError):
            calculate_cylinder_volume("2", 5)

    def test_cylinder_volume_non_number_height_raises(self):
        with self.assertRaises(TypeError):
            calculate_cylinder_volume(2, "5")

    def test_cone_volume_positive(self):
        expected = (1/3) * 3.141592653589793 * 2 ** 2 * 5
        self.assertAlmostEqual(calculate_cone_volume(2, 5), expected)

    def test_cone_volume_zero_radius(self):
        self.assertAlmostEqual(calculate_cone_volume(0, 5), 0.0)

    def test_cone_volume_zero_height(self):
        self.assertAlmostEqual(calculate_cone_volume(2, 0), 0.0)

    def test_cone_volume_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)

    def test_cone_volume_negative_height_raises(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(2, -5)

    def test_cone_volume_non_number_radius_raises(self):
        with self.assertRaises(TypeError):
            calculate_cone_volume("2", 5)

    def test_cone_volume_non_number_height_raises(self):
        with self.assertRaises(TypeError):
            calculate_cone_volume(2, "5")

    def test_cube_volume_float(self):
        self.assertAlmostEqual(calculate_cube_volume(2.5), 15.625)

    def test_sphere_volume_float(self):
        expected = (4/3) * 3.141592653589793 * 2.5 ** 3
        self.assertAlmostEqual(calculate_sphere_volume(2.5), expected)

    def test_cylinder_volume_float(self):
        expected = 3.141592653589793 * 2.5 ** 2 * 3.5
        self.assertAlmostEqual(calculate_cylinder_volume(2.5, 3.5), expected)

    def test_cone_volume_float(self):
        expected = (1/3) * 3.141592653589793 * 2.5 ** 2 * 3.5
        self.assertAlmostEqual(calculate_cone_volume(2.5, 3.5), expected)

if __name__ == '__main__':
    unittest.main()
    print(calculate_cube_volume(3))
    print(calculate_sphere_volume(3))
    print(calculate_cylinder_volume(2, 5))
    print(calculate_cone_volume(2, 5))