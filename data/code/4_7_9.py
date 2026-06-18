import unittest

class DistanceConverter:
    """A class to convert distances between different units."""

    def __init__(self, value):
        self.value = value  # Value in meters (base unit)

    @staticmethod
    def _to_meters(unit_value, source_unit):
        """Convert any given distance to meters based on the source unit."""
        conversion_factors = {
            'km': 1000,
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254,
        }

        if source_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {source_unit}")

        return value * conversion_factors[source_unit]

    def to_km(self):
        """Convert distance from meters to kilometers."""
        return self._to_meters(0.1, 'm') / 1000 if isinstance(self.value, float) else int(self.value * 0.001)

    def to_cm(self):
        """Convert distance from meters to centimeters."""
        return self._to_meters(0.01, 'cm')

    def to_mi(self):
        """Convert distance from meters to miles."""
        return self.value / 1609.34

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class."""

    def setUp(self):
        """Set up test fixtures before each test method runs."""
        pass

    def tearDown(self):
        """Clean up after each test method runs."""
        pass

    # --- Tests for to_km() ---
    def test_to_km_meters_positive_int(self):
        converter = DistanceConverter(100)  # 100m
        self.assertEqual(converter.to_km(), 0.1, "Conversion of 100 meters should be 0.1 km")

    def test_to_km_meters_float(self):
        converter = DistanceConverter(50.75)
        expected = 0.05075

if __name__ == '__main__':
    pass
