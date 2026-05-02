import unittest
def calculate_volume_box(length, width, height):
    return length * width * height
def calculate_volume_cylinder(radius, height):
    import math
    return math.pi * (radius ** 2) * height
class TestVolumeCalculations(unittest.TestCase):
    def test_calculate_volume_box_positive(self):
        self.assertEqual(calculate_volume_box(2, 3, 4), 24)
        self.assertEqual(calculate_volume_box(10, 10, 10), 1000)
    def test_calculate_volume_box_zero(self):
        self.assertEqual(calculate_volume_box(0, 5, 10), 0)
        self.assertEqual(calculate_volume_box(5, 0, 10), 0)
        self.assertEqual(calculate_volume_box(0, 0, 0), 0)
    def test_calculate_volume_box_negative(self):
        self.assertEqual(calculate_volume_box(-2, 3, 4), -24)
        self.assertEqual(calculate_volume_box(2, -3, 4), -24)
        self.assertEqual(calculate_volume_box(2, 3, -4), -24)
        self.assertEqual(calculate_volume_box(-2, -3, -4), -24)
    def test_calculate_volume_cylinder_positive(self):
        radius = 3
        height = 5
        expected = math.pi * (3 ** 2) * 5
        self.assertAlmostEqual(calculate_volume_cylinder(radius, height), expected)
        radius = 10
        height = 2
        expected = math.pi * (10 ** 2) * 2
        self.assertAlmostEqual(calculate_volume_cylinder(radius, height), expected)
    def test_calculate_volume_cylinder_zero(self):
        self.assertAlmostEqual(calculate_volume_cylinder(0, 5), 0.0)
        self.assertAlmostEqual(calculate_volume_cylinder(3, 0), 0.0)
    def test_calculate_volume_cylinder_negative(self):
        radius = -3
        height = 5
        expected = math.pi * ((-3) ** 2) * 5
        self.assertAlmostEqual(calculate_volume_cylinder(radius, height), expected)
        radius = 3
        height = -5
        expected = math.pi * (3 ** 2) * (-5)
        self.assertAlmostEqual(calculate_volume_cylinder(radius, height), expected)
if __name__ == '__main__':
    import math
    unittest.main(argv=['first-arg-is-ignored'], exit=False)