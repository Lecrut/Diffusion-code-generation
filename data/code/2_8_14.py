import unittest
import math

def calculate_sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4.0 / 3.0) * math.pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return math.pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

def calculate_rectangular_prism_volume(width, height, depth):
    if width < 0 or height < 0 or depth < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height * depth

class TestVolumeCalculations(unittest.TestCase):
    
    def test_sphere_volume_positive(self):
        result = calculate_sphere_volume(2)
        expected = (4.0 / 3.0) * math.pi * 8
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_sphere_volume_zero(self):
        result = calculate_sphere_volume(0)
        self.assertEqual(result, 0.0)
    
    def test_sphere_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)
    
    def test_cylinder_volume_positive(self):
        result = calculate_cylinder_volume(2, 5)
        expected = math.pi * 4 * 5
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_cylinder_volume_zero_radius(self):
        result = calculate_cylinder_volume(0, 5)
        self.assertEqual(result, 0.0)
    
    def test_cylinder_volume_zero_height(self):
        result = calculate_cylinder_volume(2, 0)
        self.assertEqual(result, 0.0)
    
    def test_cylinder_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-1, 5)
    
    def test_cylinder_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(2, -5)
    
    def test_cone_volume_positive(self):
        result = calculate_cone_volume(2, 5)
        expected = (1.0 / 3.0) * math.pi * 4 * 5
        self.assertAlmostEqual(result, expected, places=7)
    
    def test_cone_volume_zero_radius(self):
        result = calculate_cone_volume(0, 5)
        self.assertEqual(result, 0.0)
    
    def test_cone_volume_zero_height(self):
        result = calculate_cone_volume(2, 0)
        self.assertEqual(result, 0.0)
    
    def test_cone_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-1, 5)
    
    def test_cone_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(2, -5)
    
    def test_prism_volume_positive(self):
        result = calculate_rectangular_prism_volume(2, 3, 4)
        self.assertEqual(result, 24)
    
    def test_prism_volume_zero_width(self):
        result = calculate_rectangular_prism_volume(0, 3, 4)
        self.assertEqual(result, 0)
    
    def test_prism_volume_zero_height(self):
        result = calculate_rectangular_prism_volume(2, 0, 4)
        self.assertEqual(result, 0)
    
    def test_prism_volume_zero_depth(self):
        result = calculate_rectangular_prism_volume(2, 3, 0)
        self.assertEqual(result, 0)
    
    def test_prism_volume_negative_width(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(-1, 3, 4)
    
    def test_prism_volume_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(2, -1, 4)
    
    def test_prism_volume_negative_depth(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(2, 3, -1)

if __name__ == '__main__':
    import sys
    
    test_cases = [
        (calculate_sphere_volume, 2, None),
        (calculate_cylinder_volume, (2, 5), None),
        (calculate_cone_volume, (2, 5), None),
        (calculate_rectangular_prism_volume, (2, 3, 4), None),
    ]
    
    for func, args, _ in test_cases:
        if isinstance(args, tuple):
            val = func(*args)
        else:
            val = func(args)
        print(val)
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestVolumeCalculations)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("All unit tests passed successfully.")
    else:
        print("Some unit tests failed.")
        for failure in result.failures + result.errors:
            print(failure[1])
        sys.exit(1)