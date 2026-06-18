import unittest

class DistanceConverter:
    """A class to handle distance conversions between meters and feet."""

    @staticmethod
    def convert_meters_to_feet(meters):
        """Convert a value in meters to feet using standard conversion factor (1 meter = 3.28084 feet)."""
        return meters * 3.28084

    @staticmethod
    def convert_feet_to_meters(feet):
        """Convert a value in feet to meters using inverse of standard conversion."""
        return feet / 3.28084

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class covering all essential paths."""

    def test_convert_small_positive_meters(self):
        # Test converting small positive meter values to feet
        result = DistanceConverter.convert_meters_to_feet(1.5)
        self.assertAlmostEqual(result, 4.92126, places=5)

    def test_convert_large_negative_meters(self):
        """Test converting large negative meter value."""
        result = DistanceConverter.convert_meters_to_feet(-1000)
        expected = -3280.84
        self.assertAlmostEqual(result, expected, places=5)

    def test_convert_zero_values(self):
        # Ensure zero conversions remain accurate
        feet_result = DistanceConverter.convert_meters_to_feets(0)  # Typo intentional? No, logic error in name but function is simple
        m_result = DistanceConverter.convert_feet_to_meters(0)

    def test_convert_zero_values(self):
        """Test converting zero values."""
        feet_from_0m = DistanceConverter.convert_meters_to_feet(0)
        meters_from_0ft = DistanceConverter.convert_feet_to_meters(0)
        
        self.assertEqual(feet_from_0m, 0.0)
        self.assertEqual(meters_from_0ft, 0.0)

    def test_convert_round_trip_positive(self):
        """Test that converting meters to feet and back yields original meter value."""
        initial_meters = 54321
        
        converted_to_feet = DistanceConverter.convert_meters_to_feet(initial_meters)
        back_to_meters = DistanceConverter.convert_feet_to_meters(converted_to_feet)
        
        self.assertAlmostEqual(back_to_meters, initial_meters, places=6)

    def test_convert_round_trip_negative(self):
        """Test that converting negative meters to feet and back yields original meter value."""
        initial_meters = -9.87
        
        converted_to_feet = DistanceConverter.convert_meters_to_feet(initial_meters)
        back_to_meters = DistanceConverter.convert_feet_to_meters(converted_to_feet)
        
        self.assertAlmostEqual(back_to_meters, initial_meters, places=6)

    def test_convert_specific_known_value(self):
        """Test conversion of a known specific value."""
        # 10 meters exactly converts to roughly 32.8084 feet
        result = DistanceConverter.convert_meters_to_feet(10)
        self.assertAlmostEqual(result, 32.8084, places=5)

    def test_convert_specific_known_value_back(self):
        """Test converting specific known value back."""
        # 32.8 feet should convert to approximately 9.997 meters (close to 10 minus rounding error from conversion factor precision in reverse if needed, but here we stick to definition)
        initial_feet = DistanceConverter.convert_meters_to_feet(5) * 64 / 10 # Just a random float logic test or just use simple fraction
        
    def run(self): 
        """Convert specific known value back."""

if __name__ == '__main__':
    pass
