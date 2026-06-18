import unittest

class DistanceConverter:
    """A class to convert distance between miles and kilometers."""

    @staticmethod
    def meters_to_km(meters: float) -> float:
        return meters / 1000.0

    @staticmethod
    def km_to_miles(kilometers: float) -> float:
        # Using the precise conversion factor (1 mile = 1609.344 m)
        miles_in_km = kilometers * 0.621371192
        return miles_in_km

    @staticmethod
    def km_to_miles_approx(kilometers: float) -> float:
        # Using the standard approximation (factor of 2/3 or ~0.625 is often used, but let's stick to a common simple approx for testing variety)
        # Or better, use the reverse exact calculation from miles_in_km logic inverted roughly? 
        # Let's use the specific factor: 1 km = 0.6214 miles (standard approximation).
        return kilometers * 0.6214

class TestDistanceConverter(unittest.TestCase):

    def setUp(self) -> None:
        self.conv = DistanceConverter()

    def test_meters_to_km_exact(self):
        """Test converting meters to km with exact zero distance."""
        result = self.conv.meters_to_km(0.0)
        expected = 0.0
        self.assertEqual(result, expected)

    def test_meters_to_km_simple(self):
        """Test converting a simple integer meter value."""
        # 15 meters should be exactly 0.015 km
        result = self.conv.meters_to_km(15)
        expected = 0.015
        self.assertEqual(result, expected)

    def test_meters_to_km_large(self):
        """Test converting a large number of meters."""
        # 1 kilometer is 1000 meters -> should return exactly 1.0
        result = self.conv.meters_to_km(1000)
        expected = 1.0
        self.assertEqual(result, expected)

    def test_meters_to_km_negative(self):
        """Test converting negative meter values."""
        result = self.conv.meters_to_km(-250)
        # -250 / 1000 = -0.25
        self.assertAlmostEqual(result, -0.25, places=6)

    def test_km_to_miles_approx(self):
        """Test converting km to miles using the approximation factor."""
        result = self.conv.km_to_miles(1)
        # 1 * 0.6214
        expected = 0.6214
        self.assertAlmostEqual(result, expected, places=6)

    def test_km_to_miles_exact(self):
        """Test converting km to miles using the more precise factor."""
        result = self.conv.km_to_miles(1537)
        # Based on 1 mile = 1.609344 km -> 1537 / 1.609344
        expected = 1537 * 0.621371192
        self.assertEqual(result, expected)

    def test_km_to_miles_zero(self):
        """Test converting zero kilometers."""
        result = self.conv.km_to_miles(0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=6)

    def test_type_conversion_ints_and_floats(self):
        """Ensure the functions handle both int and float inputs correctly without errors."""
        # Test meters to km with integer input
        result1 = DistanceConverter.meters_to_km(500)  # Int -> expects float return
        self.assertIsInstance(result1, float)

        # Test km to miles with float input
        result2 = DistanceConverter.km_to_miles_approx(1.5)  # Float -> expects float return
        self.assertIsInstance(result2, float)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistanceConverter)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)