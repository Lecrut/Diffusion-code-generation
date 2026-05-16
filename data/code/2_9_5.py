import unittest
class VolumeCalculator:
    def calculate_volume_cuboid(self, length, width, height):
        return length * width * height
    def calculate_volume_sphere(self, radius):
        import math
        return (4/3) * math.pi * (radius ** 3)
class TestVolumeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = VolumeCalculator()
    def test_calculate_volume_cuboid_positive_inputs(self):
        self.assertEqual(self.calculator.calculate_volume_cuboid(2, 3, 4), 24)
        self.assertEqual(self.calculator.calculate_volume_cuboid(1, 1, 1), 1)
        self.assertEqual(self.calculator.calculate_volume_cuboid(10, 2, 5), 100)
    def test_calculate_volume_cuboid_zero_input(self):
        self.assertEqual(self.calculator.calculate_volume_cuboid(0, 5, 10), 0)
        self.assertEqual(self.calculator.calculate_volume_cuboid(5, 0, 10), 0)
        self.assertEqual(self.calculator.calculate_volume_cuboid(5, 0, 0), 0)
        self.assertEqual(self.calculator.calculate_volume_cuboid(0, 0, 0), 0)
    def test_calculate_volume_cuboid_negative_inputs(self):
        self.assertEqual(self.calculator.calculate_volume_cuboid(-2, 3, 4), -24)
        self.assertEqual(self.calculator.calculate_volume_cuboid(2, -3, 4), -24)
        self.assertEqual(self.calculator.calculate_volume_cuboid(2, 3, -4), -24)
        self.assertEqual(self.calculator.calculate_volume_cuboid(-2, -3, -4), -24)
    def test_calculate_volume_sphere_positive_input(self):
        radius = 3
        expected = (4/3) * 3 * (3 ** 3)
        self.assertAlmostEqual(self.calculator.calculate_volume_sphere(radius), expected)
    def test_calculate_volume_sphere_zero_input(self):
        radius = 0
        expected = 0.0
        self.assertAlmostEqual(self.calculator.calculate_volume_sphere(radius), expected)
    def test_calculate_volume_sphere_negative_input(self):
        radius = -2
        expected = (4/3) * math.pi * (-2 ** 3)
        self.assertAlmostEqual(self.calculator.calculate_volume_sphere(radius), expected)
if __name__ == '__main__':
    import math
    unittest.main(argv=['first-arg-is-ignored'], exit=False)