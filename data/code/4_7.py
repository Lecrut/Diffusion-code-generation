import unittest
class DistanceConverter:
    def convert_miles_to_km(self, miles):
        return miles * 1.60934
    def convert_km_to_miles(self, km):
        return km / 1.60934
class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()
        self.tolerance = 1e-5
    def test_miles_to_km_positive(self):
        miles = 10.0
        expected_km = 16.0934
        result = self.converter.convert_miles_to_km(miles)
        self.assertAlmostEqual(result, expected_km, delta=self.tolerance)
    def test_miles_to_km_zero(self):
        miles = 0.0
        expected_km = 0.0
        result = self.converter.convert_miles_to_km(miles)
        self.assertAlmostEqual(result, expected_km, delta=self.tolerance)
    def test_miles_to_km_fractional(self):
        miles = 1.5
        expected_km = 2.41401
        result = self.converter.convert_miles_to_km(miles)
        self.assertAlmostEqual(result, expected_km, delta=self.tolerance)
    def test_km_to_miles_positive(self):
        km = 16.0934
        expected_miles = 10.0
        result = self.converter.convert_km_to_miles(km)
        self.assertAlmostEqual(result, expected_miles, delta=self.tolerance)
    def test_km_to_miles_zero(self):
        km = 0.0
        expected_miles = 0.0
        result = self.converter.convert_km_to_miles(km)
        self.assertAlmostEqual(result, expected_miles, delta=self.tolerance)
    def test_km_to_miles_fractional(self):
        km = 1.60934
        expected_miles = 1.0
        result = self.converter.convert_km_to_miles(km)
        self.assertAlmostEqual(result, expected_miles, delta=self.tolerance)
    def test_conversion_round_trip(self):
        initial_miles = 50.0
        km = self.converter.convert_miles_to_km(initial_miles)
        round_trip_miles = self.converter.convert_km_to_miles(km)
        self.assertAlmostEqual(round_trip_miles, initial_miles, delta=self.tolerance)
    def test_large_values(self):
        miles = 1000.0
        expected_km = 1609.34
        result = self.converter.convert_miles_to_km(miles)
        self.assertAlmostEqual(result, expected_km, delta=self.tolerance)
        km = 1609.34
        result_miles = self.converter.convert_km_to_miles(km)
        self.assertAlmostEqual(result_miles, miles, delta=self.tolerance)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)