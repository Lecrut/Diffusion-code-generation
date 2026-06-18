import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_gallons(self):
        # Standard conversions (1 liter ≈ 0.264172 gallons)
        self.assertAlmostEqual(5 * LITERS_TO_GALLONS, 1.32086, places=5)
        self.assertAlmostEqual(10 * LITERS_TO_GALLONS, 2.64172, places=5)

    def test_convert_gallons_to_liters(self):
        # Standard conversions (1 gallon ≈ 3.78541 liters)
        self.assertAlmostEqual(5 * GALLONS_TO_LITERS, 18.92705, places=5)
        self.assertAlmostEqual(10 * GALLONS_TO_LITERS, 37.8541, places=5)

    def test_edge_case_zero_volume(self):
        # Converting zero should result in zero regardless of direction
        converted_liters = LITER_ZERO_IN_GALLONS * LITERS_TO_GALLONS
        self.assertEqual(converted_liters, 0.0)

        converted_gallons = GALLON_ZERO_IN_LITERS * GALLONS_TO_LITERS
        self.assertEqual(converted_gallons, 0.0)

    def test_large_volume_values(self):
        # Test with large numbers to ensure no floating-point overflow issues in logic flow
        large_liters = int(1e9)  # One billion liters
        converted_gallons = large_liters * LITERS_TO_GALLONS

if __name__ == '__main__':
    pass
