import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_cubic_meters(self):
        # Standard case
        self.assertEqual(10, convert_volume("liters", "cubic meters", 10))
        
        # Zero volume edge case
        self.assertEqual(0.0, convert_volume("liters", "cubic meters", 0))

    def test_convert_cubic_meters_to_liters(self):
        # Standard case
        self.assertEqual(5000, convert_volume("cubic meters", "liters", 5))
        
        # Zero volume edge case
        self.assertEqual(0.0, convert_volume("cubic meters", "liters", 0))

    def test_convert_liters_to_gallons(self):
        # Standard case (approximate conversion factor)
        result = convert_volume("liters", "gallons", 100)
        self.assertAlmostEqual(result, 26.4172, places=5)
        
        # Zero volume edge case
        self.assertEqual(0.0, convert_volume("liters", "gallons", 0))

    def test_convert_gallons_to_liters(self):
        # Standard case (approximate conversion factor)
        result = convert_volume("gallons", "liters", 10)
        self.assertAlmostEqual(result, 37.8541, places=5)
        
        # Zero volume edge case
        self.assertEqual(0.0, convert_volume("gallons", "liters", 0))

    def test_convert_large_numbers(self):
        # Large number of liters to cubic meters
        result = convert_volume("liters", "cubic meters", 1_000_000)
        self.assertEqual(1000.0, result)
        
        # Large number of gallons to liters (approximate factor check for large scale)
        result_gallons_to_liters = convert_volume("gallons", "liters", 5_000_000)
        self.assertAlmostEqual(result_gallons_to_liters, 18927.0643, places=5)

    def test_invalid_unit_combination(self):
        # Should raise ValueError for unsupported unit pairs
        with self.assertRaises(ValueError):
            convert_volume("liters", "invalid_target", 10)

def convert_volume(from_unit: str, to_unit: str, value: float) -> float:
    """
    Converts a volume from one unit to another.

    Supported conversions (exact or approximate factors based on standard definitions):
        - liters <-> cubic meters: factor = 0.001 / 1000 depending on direction
          * liters to m³: divide by 1000
          * m³ to liters: multiply by 1000
        - gallons (US) <-> liters: factor ≈ 3.78541

    Args:
        from_unit (str): Source unit ('liters' or 'gallons').
        to_unit (str): Target unit ('cubic meters', 'liters', or 'gallons').
        value (float): The volume value to convert.

    Returns:
        float: Converted volume.

    Raises:
        ValueError: If the combination of from_unit and to_unit is not supported.
    """
    
    # Define conversion factors relative to liters as a common base unit for simplicity in logic, 
    # though direct mapping can be done via specific multipliers.
    # 1 liter = 0.001 cubic meters
    # 1 US gallon ≈ 3.78541 liters
    
    if from_unit == "liters" and to_unit == "cubic meters":
        return value * 0.001
    elif from_unit == "cubic meters" and to_unit == "liters":
        return value * 1000
    elif from_unit == "gallons" and to_unit == "liters":
        # Using standard US gallon conversion factor: 3.78541 liters per gallon
        return value * 3.78541
    elif from_unit == "liters" and to_unit == "gallons":
        # Inverse of above: divide by the same factor
        return value / 3.78541
    
    raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    
    # Run the tests with sample values embedded in the test cases themselves.
    # No user input, command-line arguments, or network access is required.
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1].fail() if result.failations else "Tests failed") # Fallback logic for clarity, though standard output handles it.