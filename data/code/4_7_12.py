import unittest

class DistanceConverter:
    """A class to convert distances between various units."""
    
    def __init__(self, value_in_meters):
        self.value = float(value_in_meters) if isinstance(value_in_meters, (int, float)) else 0.0
    
    def kilometers(self):
        return self.value / 1000

    def meters(self):
        return self.value

    def centimeters(self):
        return self.value * 100

    def feet(self):
        # 1 meter = 3.28084 feet
        return self.value * 3.28084

    def yards(self):
        # 1 yard = 0.9144 meters
        return self.value / 0.9144

    def miles(self):
        # 1 mile = 1609.344 meters
        return self.value / 1609.344

class TestDistanceConverter(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up a single converter instance for all tests."""
        cls.converter = DistanceConverter(50)

    def test_kilometers_positive(self):
        expected = 50 / 1000
        self.assertAlmostEqual(self.converter.kilometers(), expected, places=2)

    def test_meters_exact_match(self):
        self.assertEqual(self.converter.meters(), 50.0)

    def test_centimeters_calculation(self):
        expected = 50 * 100
        self.assertAlmostEqual(self.converter.centimeters(), expected, delta=0.01)

    def test_feet_conversion_factor(self):
        # 50 meters is exactly ~164.042 feet
        expected = round(50 * 3.28084, 2)
        self.assertAlmostEqual(self.converter.feet(), expected, places=2)

    def test_yards_conversion_exactness(self):
        # Using the exact definition: 1 yard = 0.9144 meters exactly
        expected = round(50 / 0.9144, 3)
        self.assertAlmostEqual(self.converter.yards(), expected, places=2)

    def test_miles_precision(self):
        # 1 mile = 1609.344 meters
        expected = round(50 / 1609.344, 3)
        self.assertAlmostEqual(self.converter.miles(), expected, places=2)

    def test_negative_value_handling(self):
        """Test handling of negative distance values."""
        neg_converter = DistanceConverter(-75)
        # -75 meters -> -0.075 km
        self.assertAlmostEqual(neg_converter.kilometers(), -0.075, places=2)

    def test_zero_value_handling(self):
        """Test handling of zero distance."""
        zero_converter = DistanceConverter(0)
        # All conversions should be 0 for input 0 regardless of unit logic (mostly), 
        # except perhaps division by zero if implemented poorly. Here, all are safe.
        self.assertEqual(zero_converter.kilometers(), 0.0)
        self.assertEqual(zero_converter.meters(), 0.0)

    def test_large_value_handling(self):
        """Test handling of a large distance value."""
        large_converter = DistanceConverter(1_609_344) # Exactly 1 mile in meters
        expected_miles = 1.0
        self.assertAlmostEqual(large_converter.miles(), expected_miles, places=5)

    def test_type_conversion_int_to_float(self):
        """Ensure integer input is correctly converted to float."""
        int_input = DistanceConverter(25) # Should be treated as 25.0
        self.assertEqual(int_input.value, 25.0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistanceConverter)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(1)