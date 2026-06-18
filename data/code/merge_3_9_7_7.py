import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_cubic_meters(self):
        # Standard case
        self.assertEqual(volume_conversion("liters", "cubic meters", 10), 0.01)
        # Zero volume
        self.assertEqual(volume_conversion("liters", "cubic meters", 0), 0.0)

    def test_convert_cubic_meters_to_liters(self):
        # Standard case
        self.assertEqual(volume_conversion("cubic meters", "liters", 5), 5000)
        # Zero volume
        self.assertEqual(volume_conversion("cubic meters", "liters", 0), 0.0)

    def test_large_numbers(self):
        # Large input value for liters to cubic meters
        large_liters = 1_000_000_000
        expected_cub_meters = large_liters / 1000
        self.assertEqual(volume_conversion("liters", "cubic meters", large_liters), expected_cub_meters)

        # Large input value for cubic meters to liters
        large_cub_meters = 9_999_999_999.5
        expected_liters = large_cub_meters * 1000
        self.assertEqual(volume_conversion("cubic meters", "liters", large_cub_meters), expected_liters)

    def test_negative_numbers(self):
        # Negative volume (theoretical edge case, usually invalid but tested for robustness)
        negative_liters = -50
        expected_neg_cub_meters = negative_liters / 1000
        self.assertEqual(volume_conversion("liters", "cubic meters", negative_liters), expected_neg_cub_meters)

    def test_invalid_unit_combination(self):
        # Should raise ValueError for unsupported conversion directions
        with self.assertRaises(ValueError):
            volume_conversion("meters", "kilograms", 10)

def volume_conversion(from_unit, to_unit, value):
    """
    Convert a given volume between liters and cubic meters.

    Args:
        from_unit (str): Source unit ('liters' or 'cubic meters').
        to_unit (str): Target unit ('liters' or 'cubic meters').
        value (float/n int): Volume amount.

    Returns:
        float: Converted volume.

    Raises:
        ValueError: If units are invalid or conversion direction is not supported.
    """
    if from_unit == to_unit:
        return float(value)

    valid_units = ["liters", "cubic meters"]
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Unsupported units: {from_unit} and {to_unit}")

    conversion_rate = 0.001 if (from_unit == "liters") else 1000

    return value * conversion_rate

if __name__ == '__main__':
    # Hard-coded sample values to run the test suite without user input or external dependencies.
    unittest.main()