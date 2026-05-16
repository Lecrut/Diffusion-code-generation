import unittest
def calculate_volume_cuboid(length, width, height):
    return length * width * height
def calculate_volume_sphere(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)
class TestVolumeCalculations(unittest.TestCase):
    def test_calculate_volume_cuboid_positive(self):
        self.assertEqual(calculate_volume_cuboid(2, 3, 4), 24)
        self.assertEqual(calculate_volume_cuboid(1, 1, 1), 1)
        self.assertEqual(calculate_volume_cuboid(10, 2, 5), 100)
    def test_calculate_volume_cuboid_zero(self):
        self.assertEqual(calculate_volume_cuboid(0, 5, 10), 0)
        self.assertEqual(calculate_volume_cuboid(5, 0, 10), 0)
        self.assertEqual(calculate_volume_cuboid(0, 0, 0), 0)
    def test_calculate_volume_cuboid_negative(self):
        self.assertEqual(calculate_volume_cuboid(-2, 3, 4), -24)
        self.assertEqual(calculate_volume_cuboid(2, -3, 4), -24)
        self.assertEqual(calculate_volume_cuboid(2, 3, -4), -24)
        self.assertEqual(calculate_volume_cuboid(-2, -3, -4), -24)
    def test_calculate_volume_sphere_positive(self):
        expected = (4/3) * 3.141592653589793 * (2 ** 3)
        self.assertAlmostEqual(calculate_volume_sphere(2), expected)
        self.assertAlmostEqual(calculate_volume_sphere(1), (4/3) * math.pi)
    def test_calculate_volume_sphere_zero(self):
        self.assertAlmostEqual(calculate_volume_sphere(0), 0.0)
    def test_calculate_volume_sphere_negative(self):
        import math
        expected = (4/3) * math.pi * (-2 ** 3)
        self.assertAlmostEqual(calculate_volume_sphere(-2), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)