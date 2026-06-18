import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_zero_volume(self):
        """Test that zero input results in zero output regardless of unit."""
        self.assertEqual(convert_liters_to_gallons(0), 0)
        self.assertEqual(convert_gallons_to_liters(0, "liters"), 0.0)
        self.assertEqual(convert_gallons_to_milliliters(0), 0)

    def test_large_numbers(self):
        """Test conversion with large numerical values."""
        # Test very large input in liters to gallons
        result = convert_liters_to_gallons(1_000_000_000)
        expected_approx = 264.172052 * (1_000_000_000 / 378.541)
        self.assertAlmostEqual(result, expected_approx, places=2)

    def test_negative_volume(self):
        """Test that negative volumes are handled consistently."""
        result_liters = convert_gallons_to_liters(-10, "gallons")
        result_gallons = convert_liters_to_gallons(-378.541)
        
        # Check consistency: -10 gallons should equal approx -37.85 liters
        self.assertAlmostEqual(result_liters / 3.78541, -10, places=2)

    def test_unit_conversion(self):
        """Test conversions between different units."""
        one_gallon = convert_liters_to_gallons(3.78541)
        back_in_liters = convert_gallons_to_liters(one_gallon, "gallons")
        
        self.assertAlmostEqual(back_in_liters, 3.78541, places=2)

def convert_liters_to_gallons(liters: float) -> float:
    """Convert liters to gallons."""
    return liters / 3.78541

def convert_gallons_to_milliliters(gallons: float) -> int:
    """Convert gallons to milliliters (returns integer)."""
    return round(gallons * 3785.41)

class TestVolumeConversion(unittest.TestCase):
    def test_zero_volume(self):
        self.assertEqual(convert_liters_to_gallons(0), 0)

    def test_large_numbers(self):
        result = convert_liters_to_gallons(1_000_000_000)
        expected_approx = 264.172052 * (1_000_000_000 / 378.541)
        self.assertAlmostEqual(result, expected_approx, places=2)

    def test_negative_volume(self):
        result_liters = convert_gallons_to_liters(-10, "gallons")
        result_gallons = convert_liters_to_gallons(-378.541)
        
        self.assertAlmostEqual(result_liters / 3.78541, -10, places=2)

    def test_unit_conversion(self):
        one_gallon = convert_liters_to_gallons(3.78541)
        back_in_liters = convert_gallons_to_liters(one_gallon, "gallons")
        
        self.assertAlmostEqual(back_in_liters, 3.78541, places=2)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration and testing
    
    # Sample conversions to verify logic manually before running tests
    print("Sample Conversion Results:")
    
    zero_liters = convert_liters_to_gallons(0)
    print(f"Zero liters -> {zero_liters} gallons")

    large_volume = convert_liters_to_gallons(1_000_000_000)
    print(f"One billion liters -> {large_volume:.2f} gallons")

    negative_volume = convert_liters_to_gallons(-500)
    print(f"Negative five hundred liters -> {negative_volume:.4f} gallons")
    
    # Run the test suite with verbose output to see detailed results
    unittest.main(verbosity=2)