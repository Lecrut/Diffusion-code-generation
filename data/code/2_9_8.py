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
        expected_pi_val = 3.1415926535
        self.assertAlmostEqual(calculate_volume_cylinder(1, 1), expected_pi_val)
        self.assertAlmostEqual(calculate_volume_cylinder(2, 5), 31.415926535 * 5)
    def test_calculate_volume_cylinder_zero(self):
        self.assertEqual(calculate_volume_cylinder(0, 10), 0.0)
        self.assertEqual(calculate_volume_cylinder(5, 0), 0.0)
    def test_calculate_volume_cylinder_negative(self):
        expected_val = -31.415926535 * 5
        self.assertAlmostEqual(calculate_volume_cylinder(-1, 10), -31.415926535 * 10)
        self.assertAlmostEqual(calculate_volume_cylinder(-2, 5), -31.415926535 * 25)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)