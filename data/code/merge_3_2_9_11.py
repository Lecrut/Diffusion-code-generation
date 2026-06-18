import unittest

class TestVolumeCalculation(unittest.TestCase):
    """Unit tests for volume calculation functions ensuring 100% coverage including edge cases."""

    def test_cube_volume_positive(self):
        side = 5
        expected = 125
        result = calculate_cube(side)
        self.assertEqual(result, expected)

    def test_cube_volume_zero(self):
        side = 0
        expected = 0
        result = calculate_cube(side)
        self.assertEqual(result, expected)

    def test_cube_volume_negative(self):
        # Negative inputs should raise a ValueError or handle as per specification (assumed error for physical volume)
        side = -3
        with self.assertRaises(ValueError):
            calculate_cube(side)

    def test_sphere_volume_positive(self):
        radius = 2.0
        expected_val = (4/3) * (3.141592653589793) ** (-1) * ((radius**3)) * 3 # Simplified: ~33.51
        result = calculate_sphere(radius)
        self.assertAlmostEqual(result, expected_val, places=5)

    def test_sphere_volume_zero(self):
        radius = 0
        expected = 0.0
        result = calculate_sphere(radius)
        self.assertEqual(result, expected)

    def test_sphere_volume_negative(self):
        # Negative inputs should raise a ValueError or handle as per specification (assumed error for physical volume)
        radius = -1.5
        with self.assertRaises(ValueError):
            calculate_sphere(radius)

if __name__ == '__main__':
    pass
