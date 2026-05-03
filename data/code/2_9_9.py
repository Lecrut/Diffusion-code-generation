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
    def test_calculate_volume_box_zero_input(self):
        self.assertEqual(calculate_volume_box(0, 5, 10), 0)
        self.assertEqual(calculate_volume_box(5, 0, 10), 0)
        self.assertEqual(calculate_volume_box(5, 5, 0), 0)
        self.assertEqual(calculate_volume_box(0, 0, 0), 0)
    def test_calculate_volume_box_negative_input(self):
        self.assertEqual(calculate_volume_box(-2, 3, 4), -24)
        self.assertEqual(calculate_volume_box(2, -3, 4), -24)
        self.assertEqual(calculate_volume_box(2, 3, -4), -24)
        self.assertEqual(calculate_volume_box(-2, -3, 4), 24)
    def test_calculate_volume_cylinder_positive(self):
        expected_volume = math.pi * (1**2) * 5
        self.assertAlmostEqual(calculate_volume_cylinder(1, 5), expected_volume)
        self.assertAlmostEqual(calculate_volume_cylinder(2, 10), 40 * math.pi)
    def test_calculate_volume_cylinder_zero_input(self):
        self.assertAlmostEqual(calculate_volume_cylinder(0, 10), 0.0)
        self.assertAlmostEqual(calculate_volume_cylinder(5, 0), 0.0)
        self.assertAlmostEqual(calculate_volume_cylinder(0, 0), 0.0)
    def test_calculate_volume_cylinder_negative_input(self):
        expected_volume = math.pi * (-2**2) * 10
        self.assertAlmostEqual(calculate_volume_cylinder(-2, 10), expected_volume)
        expected_volume = math.pi * (3**2) * (-5)
        self.assertAlmostEqual(calculate_volume_cylinder(3, -5), -45 * math.pi)
        expected_volume = math.pi * (-1**2) * (-2)
        self.assertAlmostEqual(calculate_volume_cylinder(-1, -2), 2 * math.pi)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)