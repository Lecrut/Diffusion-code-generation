import unittest
class DistanceConverter:
    def convert_miles_to_km(self, miles):
        return miles * 1.60934
    def convert_km_to_miles(self, km):
        return km / 1.60934
class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()
    def test_miles_to_km_positive(self):
        self.assertAlmostEqual(self.converter.convert_miles_to_km(10), 16.0934)
        self.assertAlmostEqual(self.converter.convert_miles_to_km(0), 0.0)
        self.assertAlmostEqual(self.converter.convert_miles_to_km(1), 1.60934)
    def test_miles_to_km_zero(self):
        self.assertAlmostEqual(self.converter.convert_miles_to_km(0), 0.0)
    def test_miles_to_km_negative(self):
        self.assertAlmostEqual(self.converter.convert_miles_to_km(-5), -8.0467)
    def test_km_to_miles_positive(self):
        self.assertAlmostEqual(self.converter.convert_km_to_miles(16.0934), 10.0)
        self.assertAlmostEqual(self.converter.convert_km_to_miles(0), 0.0)
        self.assertAlmostEqual(self.converter.convert_km_to_miles(1), 0.621371)
    def test_km_to_miles_zero(self):
        self.assertAlmostEqual(self.converter.convert_km_to_miles(0), 0.0)
    def test_km_to_miles_negative(self):
        self.assertAlmostEqual(self.converter.convert_km_to_miles(-16.0934), -10.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)