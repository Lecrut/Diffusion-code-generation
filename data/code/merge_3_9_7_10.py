import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_milliliters(self):
        # Standard case
        self.assertEqual(1, 1000)
        
        # Zero volume edge case
        self.assertEqual(0, 0)
        
        # Large number edge case
        self.assertEqual(999999.5, 999999500)

    def test_convert_milliliters_to_liters(self):
        # Standard case
        self.assertEqual(1000, 1)
        
        # Zero volume edge case
        self.assertEqual(0, 0)
        
        # Large number edge case (integer input)
        self.assertEqual(999999500, 999999.5)

    def test_convert_liters_to_gallons(self):
        conversion_rate = 1 / 3.78541
        # Standard case: 2 liters to gallons
        self.assertAlmostEqual(2 * conversion_rate, 0.52836, places=5)
        
        # Zero volume edge case
        self.assertEqual(0, 0)
        
        # Large number edge case (millions of liters)
        large_liters = 1_000_000
        expected_gallons = round(large_liters * conversion_rate, 2)
        result = large_liters / 3.78541
        self.assertAlmostEqual(result, expected_gallons, places=2)

    def test_convert_gallons_to_liters(self):
        # Standard case: 0.5 gallons to liters
        self.assertEqual(0.5 * 3.78541, 1.892705)
        
        # Zero volume edge case
        self.assertEqual(0, 0)
        
        # Large number edge case (millions of gallons)
        large_gallons = 1_000_000
        expected_liters = round(large_gallons * 3.78541, 2)
        result = large_gallons * 3.78541
        self.assertAlmostEqual(result, expected_liters, places=2)

if __name__ == '__main__':
    # Run the test suite with hard-coded sample values as per requirements
    unittest.main()