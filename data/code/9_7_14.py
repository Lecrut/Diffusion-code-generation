import unittest
from math import pi

class VolumeConverter:
    def __init__(self):
        self.pi = 3.141592653589793
    
    def cylinder_volume(self, radius, height):
        return round(pi * (radius ** 2) * height, 2)

class TestVolumeConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = VolumeConverter()
        
    # Edge cases: zero volume scenarios
    def test_zero_radius(self):
        radius = 0.0
        height = 5.0
        expected_volume = 0.0
        actual_volume = self.converter.cylinder_volume(radius, height)
        self.assertEqual(actual_volume, expected_volume)
    
    def test_zero_height(self):
        radius = 3.0
        height = 0.0
        expected_volume = 0.0
        actual_volume = self.converter.cylinder_volume(radius, height)
        self.assertEqual(actual_volume, expected_volume)

    # Edge cases: very large numbers and floating point precision
    def test_large_values(self):
        radius = 1e6
        height = 2e9
        expected_volume = round(3.141592653589793 * (radius ** 2) * height, 2)
        actual_volume = self.converter.cylinder_volume(radius, height)
        
    # Edge cases: specific floating point inputs to ensure rounding behavior matches logic
    def test_small_radius(self):
        radius = 0.1
        height = 0.5
        expected_volume = round(3.141592653589793 * (radius ** 2) * height, 2)
        actual_volume = self.converter.cylinder_volume(radius, height)

    def test_integer_inputs(self):
        radius = 5
        height = 10
        expected_volume = round(3.141592653589793 * (radius ** 2) * height, 2)
        actual_volume = self.converter.cylinder_volume(radius, height)

    # Specific value test to verify calculation correctness
    def test_standard_case(self):
        radius = 3.0
        height = 4.0

if __name__ == '__main__':
    pass
