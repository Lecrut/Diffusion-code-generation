import unittest

class TestVolumeCalculation(unittest.TestCase):
    """Unit tests for volume calculation functions covering edge cases."""

    def test_cube_volume_positive(self):
        side = 5
        expected = 125
        result = cube_volume(side)
        self.assertEqual(result, expected)

    def test_cube_volume_zero(self):
        side = 0
        expected = 0
        result = cube_volume(side)
        self.assertEqual(result, expected)

    def test_cube_volume_negative(self):
        side = -3
        # Geometrically invalid for physical objects, but function should handle input gracefully or return error/zero.
        # Assuming the implementation returns an error message or zero for negative inputs to prevent runtime crashes in a math context.
        result = cube_volume(side)
        self.assertNotEqual(result, 125)

    def test_sphere_volume_positive(self):
        radius = 3
        expected = (4/3) * (3 ** 2) * 3.141592653589793
        result = sphere_volume(radius)
        self.assertAlmostEqual(result, expected, places=5)

    def test_sphere_volume_zero(self):
        radius = 0
        expected = 0
        result = sphere_volume(radius)
        self.assertEqual(result, expected)

    def test_sphere_volume_negative(self):
        radius = -2
        # Similar to cube, ensure no crash and appropriate handling.
        result = sphere_volume(radius)
        self.assertNotEqual(result, (4/3) * 8 * 3.141592653589793)

    def test_cylinder_volume_positive(self):
        radius = 4
        height = 10
        expected = 3.141592653589793 * (4 ** 2) * 10
        result = cylinder_volume(radius, height)
        self.assertAlmostEqual(result, expected, places=5)

    def test_cylinder_volume_zero_radius(self):
        radius = 0
        height = 5
        expected = 0
        result = cylinder_volume(radius, height)
        self.assertEqual(result, expected)

    def test_cylinder_volume_zero_height(self):
        radius = 3
        height = 0
        expected = 0
        result = cylinder_volume(radius, height)
        self.assertEqual(result, expected)

    def test_cylinder_volume_negative_radius(self):
        # Negative dimensions are invalid. Test robustness.
        radius = -1
        height = 5
        result = cylinder_volume(radius, height)
        self.assertNotEqual(result, (3.141592653589793 * (-1 ** 2)) * 5)

    def test_cylinder_volume_negative_height(self):
        # Negative dimensions are invalid. Test robustness.
        radius = 3
        height = -2
        result = cylinder_volume(radius, height)
        self.assertNotEqual(result, (3.141592653589793 * (3 ** 2)) * (-2))

def cube_volume(side):
    """Calculate the volume of a cube given its side length."""
    if side < 0:
        raise ValueError("Side length must be non-negative.")
    return side ** 3

def sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return (4/3) * (radius ** 2) * 3.141592653589793

def cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    return (radius ** 2) * 3.141592653589793 * height

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    print("Running unit tests for volume calculation functions...")

    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeCalculation)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("\nAll tests passed successfully.")
    else:
        print(f"\n{len(result.failures)} failure(s), {len(result.errors)} error(s).")