import unittest

class TestVolumeCalculation(unittest.TestCase):
    """Unit tests for volume calculation functions."""

    def test_cylinder_volume_positive(self):
        # Standard positive inputs
        self.assertEqual(calculate_cylinder_volume(1, 2), math.pi * (1 ** 2) * 2)

    def test_cylinder_volume_zero_radius(self):
        # Edge case: zero radius results in zero volume
        self.assertEqual(calculate_cylinder_volume(0, 5), 0.0)

    def test_cylinder_volume_negative_radius(self):
        # Edge case: negative radius squared is positive, but input validation should handle it or math handles it naturally; 
        # assuming function accepts r**2 directly without strict check on sign here for mathematical correctness unless specified otherwise.
        # However, to ensure robustness as per "edge cases like zero and negative inputs", we test the behavior.
        result = calculate_cylinder_volume(-3, 4)
        self.assertEqual(result, math.pi * ((-3) ** 2) * 4)

    def test_cone_volume_positive(self):
        # Standard positive inputs for cone
        self.assertAlmostEqual(calculate_cone_volume(10, 5), (math.pi * 10**2 * 5) / 3, places=5)

    def test_cone_volume_zero_radius(self):
        # Edge case: zero radius results in zero volume
        self.assertEqual(calculate_cone_volume(0, 8.0), 0.0)

    def test_cone_volume_negative_radius(self):
        # Edge case: negative radius input handled mathematically (r^2 is positive) or validated by function logic if any exists.
        result = calculate_cone_volume(-6.5, 12.3)
        expected = (math.pi * ((-6.5)**2) * 12.3) / 3
        self.assertAlmostEqual(result, expected, places=5)

    def test_sphere_volume_positive(self):
        # Standard positive inputs for sphere
        self.assertEqual(calculate_sphere_volume(7), math.pi * (7 ** 3) * (4/3))

    def test_sphere_volume_zero_radius(self):
        # Edge case: zero radius results in zero volume
        self.assertEqual(calculate_sphere_volume(0.0), 0.0)

    def test_sphere_volume_negative_radius(self):
        # Edge case: negative radius input handled mathematically (r^3 sign matters, but typically radius is non-negative)
        result = calculate_sphere_volume(-2)
        expected = math.pi * ((-2)**3) * (4/3)
        self.assertEqual(result, expected)

def calculate_cylinder_volume(radius: float, height: float) -> float:
    return math.pi * radius**2 * height

def calculate_cone_volume(radius: float, height: float) -> float:
    return (math.pi * radius**2 * height) / 3

def calculate_sphere_volume(radius: float) -> float:
    return math.pi * radius**3 * (4/3)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or files
    import sys

    # Run the tests directly with a custom test runner if desired, 
    # but here we just invoke unittest.main() which reads from the module's TestCase methods.
    
    # To ensure no external dependencies like argparse are used and it runs standalone:
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeCalculation)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if not result.wasSuccessful():
            sys.exit(1)
    except Exception as e:
        print(f"Error during test execution: {e}")
        sys.exit(1)