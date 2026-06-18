import unittest

class VolumeConversionTests(unittest.TestCase):
    """Test suite for volume conversion logic covering edge cases."""

    def test_convert_liters_to_milliliters(self):
        """Convert liters to milliliters (1 L = 1000 mL)."""
        self.assertEqual(convert_volume(0, 'l', 'ml'), 0)
        self.assertEqual(convert_volume(1.5, 'l', 'ml'), 1500)
        self.assertEqual(convert_volume(-2.3, 'l', 'ml'), -2300)

    def test_convert_milliliters_to_liters(self):
        """Convert milliliters to liters (1 L = 1000 mL)."""
        self.assertEqual(convert_volume(0, 'ml', 'l'), 0)
        self.assertEqual(convert_volume(500, 'ml', 'l'), 0.5)
        self.assertEqual(convert_volume(-750, 'ml', 'l'), -0.75)

    def test_convert_liters_to_gallons(self):
        """Convert liters to gallons (1 L ≈ 0.264172 gal)."""
        self.assertEqual(convert_volume(0, 'l', 'gal'), 0)
        # Test with a value that results in an exact expected float within tolerance if needed, 
        # but here we rely on standard precision for the sample run without external deps.
        result = convert_volume(10, 'l', 'gal')
        self.assertAlmostEqual(result, 2.64172)

    def test_convert_gallons_to_liters(self):
        """Convert gallons to liters (1 L ≈ 3.78541 gal)."""
        self.assertEqual(convert_volume(0, 'gal', 'l'), 0)
        # Test with a value that results in an exact expected float within tolerance if needed, 
        # but here we rely on standard precision for the sample run without external deps.
        result = convert_volume(10, 'gal', 'l')
        self.assertAlmostEqual(result, 37.8541)

    def test_large_numbers(self):
        """Test conversion with very large numbers."""
        # Large number of liters to milliliters
        large_liters = 999_999_000
        expected_ml = large_liters * 1000
        self.assertEqual(convert_volume(large_liters, 'l', 'ml'), expected_ml)

    def test_large_numbers_reverse(self):
        """Test conversion with very large numbers (reverse)."""
        # Large number of milliliters to liters
        large_ml = 987_654_321_000
        result_l = convert_volume(large_ml, 'ml', 'l')
        self.assertAlmostEqual(result_l, 987654.321)

# Helper function definition (simulating the logic from a previous step for completeness in this file)
def convert_volume(volume: float, unit_from: str, unit_to: str) -> float:
    """Convert volume between different units."""
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be an int or float")

    # Define conversion factors relative to base liters for simplicity in this standalone file
    # 1 liter = 1000 ml
    # 1 gallon ≈ 3.78541 liters
    
    if unit_from == 'l' and unit_to == 'ml':
        return volume * 1000
    elif unit_from == 'ml' and unit_to == 'l':
        return volume / 1000
    elif unit_from == 'l' and unit_to == 'gal':
        return volume * 0.264172
    elif unit_from == 'gal' and unit_to == 'l':
        return volume * 3.78541
    
    raise ValueError(f"Unsupported conversion: {unit_from} to {unit_to}")

if __name__ == '__main__':
    # Run tests with hard-coded sample values as per requirement
    suite = unittest.TestLoader().loadTestsFromTestCase(VolumeConversionTests)
    
    # Optional: Print results directly if not using a runner, but standard practice is unittest.main() or similar.
    # However, to ensure it runs without command line args and produces output cleanly in this context:
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    exit(result.wasSuccessful())