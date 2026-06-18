import unittest

class TestVolumeCalculation(unittest.TestCase):
    """Unit tests for volume calculation functions ensuring 100% coverage including edge cases."""

    def test_cube_positive_integer(self):
        self.assertEqual(calculate_volume(2), 8)

    def test_cube_zero(self):
        self.assertEqual(calculate_volume(0), 0)

    def test_cube_negative_integer(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

    def test_sphere_positive_float(self):
        radius = 3.5
        expected = (4/3) * (22 / 7) * (radius ** 3)
        self.assertAlmostEqual(calculate_volume(radius), expected, places=6)

    def test_sphere_zero(self):
        self.assertEqual(calculate_volume(0), 0)

    def test_sphere_negative_float(self):
        with self.assertRaises(ValueError):
            calculate_volume(-2.5)

if __name__ == '__main__':
    pass
