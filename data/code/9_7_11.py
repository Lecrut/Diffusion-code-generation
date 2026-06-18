import unittest

class TestVolumeConversion(unittest.TestCase):
    """Test suite for volume conversion logic covering edge cases."""

    def test_convert_liters_to_milliliters_zero(self):
        # Edge case: Zero input should result in zero output
        self.assertEqual(convert_volume(0, "liters", "milliliters"), 0)

    def test_convert_liters_to_gallons_large_number(self):
        # Test with a large number of liters to ensure no overflow or precision loss issues
        large_liters = 1_000_000
        expected_gallons = convert_volume(large_liters, "liters", "gallons")
        self.assertEqual(expected_gallons, round(264.1720512415655 * large_liters))

    def test_convert_milliliters_to_liters_zero(self):
        # Edge case: Zero milliliters should result in zero liters
        self.assertEqual(convert_volume(0, "milliliters", "liters"), 0)

    def test_convert_gallons_to_liters_large_number(self):
        # Test with a large number of gallons
        large_gallons = 1_000_000
        expected_liters = convert_volume(large_gallons, "gallons", "liters")
        self.assertEqual(expected_liters, round(3.785411784 * large_gallons))

    def test_convert_invalid_unit_raises_error(self):
        # Ensure invalid units raise an appropriate error
        with self.assertRaises(ValueError):
            convert_volume(10, "invalid", "liters")

def convert_volume(volume: float, from_unit: str, to_unit: str) -> float:
    """Convert volume between liters and gallons.

    Args:
        volume (float): The volume value.
        from_unit (str): Source unit ('liters' or 'milliliters').
        to_unit (str): Target unit ('gallons', 'liters', or 'milliliters').

    Returns:
        float: Converted volume.

    Raises:
        ValueError: If units are invalid.
    """
    if from_unit not in ("liters", "milliliters") or to_unit not in (
        "gallons",
        "liters",
        "milliliters",
    ):
        raise ValueError("Invalid unit specified.")

    # Conversion factors relative to liters: 1 liter = 0.264172 gallons, 1 liter = 1000 milliliters
    if from_unit == "liters":
        value_in_liters = volume
    elif from_unit == "milliliters":
        value_in_liters = volume / 1000

    # Convert to target unit
    if to_unit == "gallons":
        return round(value_in_liters * 0.264172, 5)
    elif to_unit == "liters":
        return value_in_liters
    else:  # milliliters
        return round(value_in_liters * 1000, 2)

if __name__ == "__main__":
    # Hard-coded sample values for demonstration without user input or external dependencies
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else result.errors[0][1])