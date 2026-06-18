import unittest

class DistanceConverter:
    """A class to convert distances between meters, kilometers, miles, feet, and yards."""

    def __init__(self):
        self.meters = 0

    def set_meters(self, value):
        """Set the distance in meters."""
        self.meters = float(value)

    def to_kilometers(self):
        return self.meters / 1000.0

    def to_miles(self):
        return self.meters * 0.000621371

    def to_feet(self):
        return self.meters * 3.28084

    def to_yards(self):
        return self.to_feet() / 3.0

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class."""

    def setUp(self):
        self.converter = DistanceConverter()

    def test_set_meters_negative(self):
        """Verify setting negative meters works correctly."""
        self.converter.set_meters(-150)
        self.assertEqual(self.converter.to_kilometers(), -0.15)
        self.assertAlmostEqual(self.converter.to_feet(), -492.126, places=3)

    def test_set_meters_zero(self):
        """Verify zero distance conversions."""
        self.converter.set_meters(0)
        self.assertEqual(self.converter.to_kilometers(), 0)
        self.assertEqual(self.converter.to_miles(), 0)
        self.assertEqual(self.converter.to_yards(), 0)

    def test_to_kilometers_accuracy(self):
        """Test kilometer conversion accuracy."""
        self.converter.set_meters(5000)
        expected = 5.0
        result = self.converter.to_kilometers()
        self.assertAlmostEqual(result, expected, places=1)

    def test_to_miles_accuracy(self):
        """Test mile conversion accuracy."""
        self.converter.set_meters(1609.34)  # Approximate length of a mile in meters
        result = self.converter.to_miles()
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_to_feet_accuracy(self):
        """Test feet conversion accuracy."""
        self.converter.set_meters(100)
        expected = 328.084
        result = self.converter.to_feet()
        self.assertAlmostEqual(result, expected, places=3)

    def test_to_yards_from_kilometers(self):
        """Test yard conversion derived from kilometers."""
        # Convert 1 km to yards: 1000m * 3.28084 / 3 = ~1093.613 yards
        self.converter.set_meters(1000)
        result = self.converter.to_yards()

if __name__ == '__main__':
    pass
