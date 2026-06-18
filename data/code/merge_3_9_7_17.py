import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_cubic_meters(self):
        # Standard case
        self.assertEqual(10, convert_volume("liters", 5))
        
    def test_convert_cubic_meters_to_liters(self):
        # Reverse direction
        self.assertEqual(2.5, convert_volume("cubic meters", 3))

    def test_edge_case_zero_volume(self):
        """Test handling of zero volume."""
        result = convert_volume("liters", 0)
        assert abs(result - 0) < 1e-9
        
    def test_large_numbers(self):
        """Test conversion with large numerical values."""
        # Large liters to cubic meters
        large_liters = 5_000_000_000
        result_l_to_m3 = convert_volume("liters", large_liters)
        expected_m3 = large_liters / 1000.0
        self.assertAlmostEqual(result_l_to_m3, expected_m3)

    def test_small_numbers(self):
        """Test conversion with very small numerical values."""
        # Small liters to cubic meters (e.g., milliliter scale approximated in liters)
        tiny_liters = 1e-6
        result_l_to_m3 = convert_volume("liters", tiny_liters)
        expected_m3 = tiny_liters / 1000.0
        self.assertAlmostEqual(result_l_to_m3, expected_m3)

    def test_negative_values(self):
        """Test handling of negative volume values."""
        result = convert_volume("liters", -50)
        assert abs(result + 0.05) < 1e-9

def convert_volume(unit: str, value: float) -> float:
    """Convert a given volume to cubic meters based on the input unit.

    Args:
        unit (str): The source unit ('liters' or 'cubic_meters').
        value (float): The numerical value of the volume in the specified unit.

    Returns:
        float: The converted volume in cubic meters.
    
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if unit.lower() == "liters":
        return value / 1000.0
    elif unit.lower() == "cubic_meters":
        return value * 1000.0
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    # Hard-coded sample values to run the tests without user input or external dependencies
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else "Error in test execution")