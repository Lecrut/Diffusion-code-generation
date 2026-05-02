import unittest
def calculate_volume_box(length, width, height):
    return length * width * height
def calculate_volume_cylinder(radius, height):
    import math
    return math.pi * (radius ** 2) * height
class TestVolumeCalculations(unittest.TestCase):
    def test_calculate_volume_box_positive(self):
        self.assertEqual(calculate_volume_box(2, 3, 4), 24)
        self.assertEqual(calculate_volume_box(10, 5, 2), 100)
    def test_calculate_volume_box_zero_input(self):
        self.assertEqual(calculate_volume_box(0, 5, 10), 0)
        self.assertEqual(calculate_volume_box(10, 0, 5), 0)
        self.assertEqual(calculate_volume_box(0, 0, 0), 0)
    def test_calculate_volume_box_negative_input(self):
        self.assertEqual(calculate_volume_box(-2, 3, 4), -24)
        self.assertEqual(calculate_volume_box(2, -3, 4), -24)
        self.assertEqual(calculate_volume_box(2, 3, -4), -24)
        self.assertEqual(calculate_volume_box(-2, -3, 4), 24)
    def test_calculate_volume_cylinder_positive(self):
        expected_volume = 3.14159 * (1**2) * 5
        self.assertAlmostEqual(calculate_volume_cylinder(1, 5), expected_volume)
        self.assertAlmostEqual(calculate_volume_cylinder(2, 10), 125.6636)
    def test_calculate_volume_cylinder_zero_input(self):
        self.assertAlmostEqual(calculate_volume_cylinder(0, 10), 0.0)
        self.assertAlmostEqual(calculate_volume_cylinder(5, 0), 0.0)
    def test_calculate_volume_cylinder_negative_input(self):
        self.assertAlmostEqual(calculate_volume_cylinder(-1, 5), -15.70796)
        self.assertAlmostEqual(calculate_volume_cylinder(1, -5), -15.70796)
        self.assertAlmostEqual(calculate_volume_cylinder(-1, -5), 15.70796)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)