import unittest

class DistanceConverter:
    """A class to convert distances between various units."""

    def __init__(self, value_in_meters):
        self.value = value_in_meters  # Store in meters as the base unit

    def to_kilometers(self) -> float:
        return self.value / 1000.0

    def to_feet(self) -> float:
        return self.value * 3.28084

    def to_miles(self) -> float:
        return self.value / 1609.34

    def to_inches(self) -> float:
        return self.value * 39.3701

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class."""

    def setUp(self):
        # Initialize converter with a base value of 5 meters for most tests
        self.converter = DistanceConverter(5)

    def test_to_kilometers_exact(self):
        result = self.converter.to_kilometers()
        expected = 0.005
        self.assertEqual(result, expected)

    def test_to_feet_approximate(self):
        # Using approximate conversion factor for floating point comparison with tolerance
        result = self.converter.to_feet()
        expected = 16.4042
        self.assertAlmostEqual(result, expected, places=5)

    def test_to_miles_exact(self):
        result = self.converter.to_miles()
        # 5 / 1609.34 is approximately 0.003107... 
        # We use assertAlmostEqual for floating point precision here as well, but checking logic path first
        expected_approx = 0.003107
        self.assertAlmostEqual(result, expected_approx, places=5)

    def test_to_inches_exact(self):
        result = self.converter.to_inches()
        # 5 * 39.3701 is exactly 196.8505 based on the defined constant in class logic simulation
        expected = 196.8505
        self.assertEqual(result, expected)

    def test_conversion_from_zero(self):
        zero_converter = DistanceConverter(0)
        self.assertAlmostEqual(zero_converter.to_kilometers(), 0.0)
        self.assertAlmostEqual(zero_converter.to_feet(), 0.0)
        self.assertAlmostEqual(zero_converter.to_miles(), 0.0)
        self.assertEqual(zero_converter.to_inches(), 0.0)

    def test_conversion_from_large_value(self):
        large_converter = DistanceConverter(160934) # Exactly one mile in meters approx based on constant used
        result_km = large_converter.to_kilometers()
        expected_km = 160.934
        self.assertAlmostEqual(result_km, expected_km, places=5)

    def test_conversion_from_large_value_to_miles(self):
        # Using the same value as above to verify round trip logic roughly
        converter = DistanceConverter(160934)
        result_mi = converter.to_miles()
        self.assertAlmostEqual(result_mi, 1.0, places=5)

    def test_conversion_from_large_value_to_inches(self):
        large_converter = DistanceConverter(160934)
        expected_inches = 6372840 # Calculated as 160934 * 39.3701
        self.assertEqual(large_converter.to_inches(), expected_inches)

if __name__ == '__main__':
    # Hard-coded sample values and test execution without user input or external dependencies
    
    # Sample data for manual verification if needed (though tests are automated here)
    samples = [
        {"meters": 5, "expected_km": 0.005},
        {"meters": 160934, "expected_miles_approx": 1.0},
        {"meters": 0, "expected_inches": 0},
    ]

    # Run the test suite with verbose output to ensure all paths are covered
    unittest.main(exit=False)