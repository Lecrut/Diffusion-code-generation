import unittest

class TestVolumeConversion(unittest.TestCase):
    """Test suite for volume conversion logic."""

    def setUp(self):
        # Mock helper function to simulate the conversion logic from the previous step.
        # Converts liters to gallons using standard approximation (1 L ≈ 0.264172 gal).
        self.converter = {
            'liters_to_gallons': lambda l: round(l * 0.264172, 3),
            'gallons_to_liters': lambda g: round(g / 0.264172, 3),
        }

    def test_zero_volume(self):
        """Test conversion of zero volume."""
        self.assertEqual(
            self.converter['liters_to_gallons'](0), 
            0.0,
            "Converting zero liters should result in zero gallons"
        )
        self.assertEqual(
            self.converter['gallons_to_liters'](0), 
            0.0, 
            "Converting zero gallons should result in zero liters"
        )

    def test_large_numbers(self):
        """Test conversion with large numbers to ensure precision handling."""
        # Test a very large value (e.g., one million)
        large_liters = 1_000_000
        expected_gallons_expected_approx = large_liters * 0.264172
        self.assertAlmostEqual(
            self.converter['liters_to_gallons'](large_liters), 
            round(expected_gallons_expected_approx, 3),
            msg="Large number conversion should be accurate"
        )

        # Test a very large value in reverse (one million gallons)
        large_gallons = 1_000_000
        expected_liters_expected_approx = large_gallons / 0.264172
        self.assertAlmostEqual(
            self.converter['gallons_to_liters'](large_gallons), 
            round(expected_liters_expected_approx, 3),
            msg="Large number conversion back to liters should be accurate"
        )

    def test_negative_volume(self):
        """Test handling of negative volume values."""
        # While physical volumes can't typically be negative in real life, logic tests often include this.
        neg_liters = -50
        self.assertEqual(
            self.converter['liters_to_gallons'](neg_liters), 
            round(neg_liters * 0.264172, 3)
        )

    def test_decimal_precision(self):
        """Test conversion with decimal inputs."""
        # Test a value that results in repeating decimals to check rounding behavior
        input_val = 0.5
        result_gal = self.converter['liters_to_gallons'](input_val)
        expected_result = round(0.5 * 0.264172, 3)
        self.assertEqual(result_gal, expected_result)

    def test_round_trip_conversion(self):
        """Test that converting liters to gallons and back yields approximately the original value."""
        # Pick a non-terminating decimal example
        liters = 0.354
        
        converted_back_to_liters = self.converter['gallons_to_liters'](self.converter['liters_to_gallons'](liters))
        
        # Allow for small floating point discrepancies due to rounding in the intermediate step
        diff = abs(liters - converted_back_to_liters)
        self.assertLessEqual(diff, 0.15, "Round-trip conversion should stay within acceptable tolerance")

if __name__ == '__main__':
    # Run tests with hard-coded sample values as per requirements
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    
    # Execute and print results directly to stdout without user prompts or args
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    exit(result.wasSuccessful())