import unittest

class DistanceConverter:
    """A class to convert distances between different units."""
    
    def __init__(self, value_in_meters):
        self.value = value_in_meters  # Base unit is meters
    
    def to_kilometers(self) -> float:
        return self.value / 1000.0
    
    def to_miles(self) -> float:
        return self.value * 0.000621371
    
    def to_feet(self) -> float:
        return self.value * 3.28084
    
    def to_inches(self) -> float:
        return self.to_feet() * 12

class TestDistanceConverter(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        # Using a standard distance for testing (e.g., length of a football field is ~90 meters, 
        # but we use exactly 500 meters to avoid floating point edge cases in simple math)
        self.converter = DistanceConverter(500.0)

    def test_to_kilometers_exact(self):
        """Test conversion from meters to kilometers."""
        expected = 0.5
        result = self.converter.to_kilometers()
        self.assertEqual(result, expected)

    def test_to_miles_approximate(self):
        """Test conversion from meters to miles with approximate value check."""
        # 500 * 0.000621371 = 0.3106855
        result = self.converter.to_miles()
        expected = 0.3106855
        self.assertAlmostEqual(result, expected)

    def test_to_feet_exact(self):
        """Test conversion from meters to feet."""
        # 500 * 3.28084 = 1640.42
        result = self.converter.to_feet()
        expected = 1640.42
        self.assertEqual(result, expected)

    def test_to_inches_exact(self):
        """Test conversion from meters to inches."""
        # 500 * 3.28084 * 12 = 19685.04
        result = self.converter.to_inches()
        expected = 19685.04
        self.assertEqual(result, expected)

    def test_conversion_from_zero(self):
        """Test conversion when input is zero."""
        converter_zero = DistanceConverter(0.0)
        
        # Zero meters should be exactly zero in any unit
        self.assertEqual(converter_zero.to_kilometers(), 0.0)
        self.assertAlmostEqual(converter_zero.to_miles(), 0.0, places=5)
        self.assertEqual(converter_zero.to_feet(), 0.0)
        self.assertEqual(converter_zero.to_inches(), 0.0)

    def test_conversion_from_large_value(self):
        """Test conversion with a larger input value (1 kilometer = 1000 meters)."""
        converter_km = DistanceConverter(1000.0)
        
        # Should return exactly 1.0 km
        self.assertEqual(converter_km.to_kilometers(), 1.0)
        expected_miles = 1000 * 0.000621371
        self.assertAlmostEqual(converter_km.to_miles(), expected_miles, places=5)

    def test_negative_value_handling(self):
        """Test conversion with a negative value."""
        converter_neg = DistanceConverter(-500.0)
        
        # Negative meters should yield consistent negative results in all units
        self.assertEqual(converter_neg.to_kilometers(), -0.5)
        expected_miles = -500 * 0.000621371
        self.assertAlmostEqual(converter_neg.to_miles(), expected_miles, places=5)

if __name__ == '__main__':
    # Hard-coded sample values are embedded in the setUp method and test cases above.
    # No user input, command-line arguments, or network access is required.
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistanceConverter)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed
    exit(result.wasSuccessful() and 0 or 1)