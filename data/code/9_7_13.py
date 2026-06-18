import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_milliliters(self):
        """Tests conversion from liters to milliliters with various inputs including edge cases."""
        
        # Standard conversions
        self.assertEqual(convert_volume(0, 'l', 'ml'), 0)
        self.assertEqual(convert_volume(1, 'l', 'ml'), 1000)
        self.assertEqual(convert_volume(-5.5, 'l', 'ml'), -5500)

    def test_convert_milliliters_to_liters(self):
        """Tests conversion from milliliters to liters with various inputs including edge cases."""
        
        # Standard conversions
        self.assertEqual(convert_volume(1000, 'ml', 'l'), 1.0)
        self.assertEqual(convert_volume(500, 'ml', 'l'), 0.5)
        self.assertEqual(convert_volume(-2500, 'ml', 'l'), -2.5)

    def test_convert_liters_to_gallons(self):
        """Tests conversion from liters to gallons."""
        
        # Standard conversions (1 liter ≈ 0.264172 gallons)
        self.assertEqual(convert_volume(3.785, 'l', 'gal'), 1.0)
        self.assertEqual(convert_volume(0, 'l', 'gal'), 0)

    def test_convert_gallons_to_liters(self):
        """Tests conversion from gallons to liters."""
        
        # Standard conversions (1 gallon ≈ 3.78541 liters)
        self.assertEqual(convert_volume(2, 'gal', 'l'), 7.57082)

    def test_invalid_unit_conversion_raises_error(self):
        """Tests that invalid unit combinations raise a ValueError."""
        
        with self.assertRaises(ValueError):
            convert_volume(10, 'kg', 'ml')

def convert_volume(volume: float, from_unit: str, to_unit: str) -> float:
    """
    Converts volume between liters (l), milliliters (ml), and gallons (gal).

    Args:
        volume (float): The volume value. Can be zero or negative.
        from_unit (str): Source unit ('l', 'ml', 'gal').
        to_unit (str): Target unit ('l', 'ml', 'gal').

    Returns:
        float: Converted volume.

    Raises:
        ValueError: If units are invalid or conversion is not supported directly without intermediate step.
    
    Note: Direct conversions between ml and gal require passing through liters for precision, 
             though the logic handles direct calls by normalizing to an internal base if needed.
             For this specific implementation context assuming a helper function exists that does full normalization:
    """
    # Assuming existence of a robust underlying conversion mechanism or simplified math here based on previous steps' context.
    # Since I cannot see "previous step", I will implement the logic inline to ensure it is self-contained and runnable.

    if from_unit == 'l':
        if to_unit == 'ml':
            return volume * 1000
        elif to_unit == 'gal':
            return volume / 3.785411784
    
    elif from_unit == 'ml':
        if to_unit == 'l':
            return volume / 1000
        elif to_unit == 'gal':
            # Convert ml -> l -> gal
            liters = volume / 1000
            return liters / 3.785411784

    elif from_unit == 'gal':
        if to_unit == 'l':
            return volume * 3.785411784
        elif to_unit == 'ml':
            # Convert gal -> l -> ml
            liters = volume * 3.785411784
            return liters * 1000

    else:
        raise ValueError(f"Unsupported unit '{from_unit}' or target unit '{to_unit}'. Supported units are 'l', 'ml', 'gal'.")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input, command-line arguments, network access, or pre-existing files.
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else result.errors[0][1]) # Print error details on failure for debugging clarity in console, though standard behavior handles it.