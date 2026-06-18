import unittest

class DistanceConverter:
    """A class to convert distances between different units."""
    
    def __init__(self, value_in_meters):
        self.value = value_in_meters
    
    def to_kilometers(self) -> float:
        return self.value / 1000.0

    def to_feet(self) -> float:
        # 1 meter = 3.28084 feet
        return self.value * 3.28084

    def to_miles(self) -> float:
        # 1 kilometer = 0.621371 miles, so 1 meter = 0.000621371 miles
        km = self.to_kilometers()
        return km * 0.621371

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class."""

    def setUp(self) -> None:
        # Create a converter with base value of 5 meters for consistent testing
        self.converter = DistanceConverter(5)

    def test_to_kilometers_exact(self):
        """Verify conversion from meters to kilometers yields exact result."""
        expected = 0.005
        actual = self.converter.to_kilometers()
        self.assertEqual(actual, expected)

    def test_to_feet_approximation(self):
        """Verify conversion from meters to feet with known approximation."""
        # 5 * 3.28084 = 16.4042
        expected = 16.4042
        actual = self.converter.to_feet()
        self.assertAlmostEqual(actual, expected, places=4)

    def test_to_miles_approximation(self):
        """Verify conversion from meters to miles with known approximation."""
        # (5 / 1000) * 0.621371 = 0.003106855
        expected = 0.003106855
        actual = self.converter.to_miles()
        self.assertAlmostEqual(actual, expected, places=4)

    def test_conversion_chain(self):
        """Verify that converting meters -> kilometers -> miles is consistent."""
        # Direct to miles vs Meters->Kilometers then Kilometers->Miles logic check
        direct = self.converter.to_miles()
        via_km = (self.converter.value / 1000.0) * 0.621371
        self.assertEqual(direct, via_km)

    def test_large_value_conversion(self):
        """Test with a larger value to ensure no overflow or precision issues."""
        large_meters = 500000
        converter = DistanceConverter(large_meters)
        
        # Expected kilometers: 500 km
        expected_km = 500.0
        actual_km = converter.to_kilometers()
        self.assertEqual(actual_km, expected_km)

    def test_small_value_conversion(self):
        """Test with a very small value (less than one meter)."""
        small_meters = 1e-6
        converter = DistanceConverter(small_meters)
        
        # Expected kilometers: 0.000001 km
        expected_km = 1e-9
        actual_km = converter.to_kilometers()
        self.assertEqual(actual_km, expected_km)

    def test_negative_value_conversion(self):
        """Test with a negative value (theoretically possible in some contexts)."""
        neg_meters = -50.0
        converter = DistanceConverter(neg_meters)
        
        # Expected kilometers: -0.05 km
        expected_km = -0.05
        actual_km = converter.to_kilometers()
        self.assertEqual(actual_km, expected_km)

    def test_feet_precision(self):
        """Verify feet conversion maintains reasonable precision."""
        meters = 1234.56789
        converter = DistanceConverter(meters)
        
        # Manual calculation: 1234.56789 * 3.28084
        expected_feet = round(1234.56789 * 3.28084, 4)
        actual_feet = converter.to_feet()
        
        self.assertAlmostEqual(actual_feet, expected_feet, places=4)

if __name__ == '__main__':
    # Hard-coded sample values are embedded directly in the test cases above (5 meters).
    # No user input or external dependencies required.
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistanceConverter)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failIfNoSuccesses())