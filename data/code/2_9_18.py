import unittest

class TestVolumeCalculation:
    """Unit tests for volume calculation functions."""

    def test_cube_volume_positive(self):
        # Standard positive integer input
        self.assertEqual(27, calculate_cube_volume(3))

    def test_cube_volume_float(self):
        # Positive float input
        self.assertAlmostEqual(calculate_cube_volume(4.5), 91.125)

    def test_sphere_volume_positive(self):
        # Standard positive radius
        self.assertAlmostEqual(calculate_sphere_volume(1), 4/3 * (3.141592653589793))

    def test_cylinder_volume_positive(self):
        # Positive radius and height
        r = 2
        h = 5
        expected = 3.141592653589793 * (r ** 2) * h
        self.assertAlmostEqual(calculate_cylinder_volume(r, h), expected)

    def test_cube_volume_zero(self):
        # Zero input for cube volume
        result = calculate_cube_volume(0)
        self.assertEqual(result, 0.0)

    def test_sphere_volume_zero(self):
        # Zero radius for sphere volume
        result = calculate_sphere_volume(0)
        self.assertAlmostEqual(result, 0.0)

    def test_cylinder_volume_zero_radius(self):
        # Zero radius for cylinder volume (should be zero regardless of height)
        h = 10
        expected = 3.141592653589793 * (0 ** 2) * h
        self.assertAlmostEqual(calculate_cylinder_volume(0, h), expected)

    def test_cube_volume_negative(self):
        # Negative input for cube volume (should raise ValueError or handle gracefully based on spec; here we expect error as negative length is physically impossible but mathematically valid in some contexts. Assuming strict physical constraint check.)
        with self.assertRaises(ValueError):
            calculate_cube_volume(-2)

    def test_sphere_volume_negative(self):
        # Negative radius for sphere volume (should raise ValueError)
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-1)

    def test_cylinder_volume_negative_radius(self):
        # Negative radius for cylinder volume (should raise ValueError)
        h = 5
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-2, h)

    def test_cylinder_volume_negative_height(self):
        # Negative height for cylinder volume (should raise ValueError)
        r = 3
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(r, -4)

def calculate_cube_volume(side_length: float) -> float:
    """Calculate the volume of a cube given its side length."""
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return (side_length ** 3)

def calculate_sphere_volume(radius: float) -> float:
    """Calculate the volume of a sphere given its radius."""
    PI = 3.141592653589793
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return (4/3) * PI * (radius ** 3)

def calculate_cylinder_volume(radius: float, height: float) -> float:
    """Calculate the volume of a cylinder given its radius and height."""
    PI = 3.141592653589793
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    return PI * (radius ** 2) * height

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    
    print("--- Running Unit Tests ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeCalculation)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed, though the task asks for a runnable module.
    # We print success/failure status explicitly here as part of the sample block logic.
    
    if not result.wasSuccessful():
        print("Some tests failed.")
    else:
        print("All tests passed successfully.")