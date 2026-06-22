import unittest

class DistanceConverter:
    def __init__(self):
        self.meters_to_feet = 3.28084
        self.feet_to_meters = 1 / self.meters_to_feet
        self.kilometers_to_miles = 0.621371
        self.miles_to_kilometers = 1 / self.kilometers_to_miles

    def meters_to_feet_conversion(self, meters):
        return meters * self.meters_to_feet

    def feet_to_meters_conversion(self, feet):
        return feet * self.feet_to_meters

    def kilometers_to_miles_conversion(self, kilometers):
        return kilometers * self.kilometers_to_miles

    def miles_to_kilometers_conversion(self, miles):
        return miles * self.miles_to_kilometers

class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()

    def test_meters_to_feet(self):
        self.assertAlmostEqual(self.converter.meters_to_feet_conversion(1), 3.28084)
        self.assertAlmostEqual(self.converter.meters_to_feet_conversion(0), 0)
        self.assertAlmostEqual(self.converter.meters_to_feet_conversion(10), 32.8084)

    def test_feet_to_meters(self):
        self.assertAlmostEqual(self.converter.feet_to_meters_conversion(1), 0.3048)
        self.assertAlmostEqual(self.converter.feet_to_meters_conversion(0), 0)
        self.assertAlmostEqual(self.converter.feet_to_meters_conversion(32.8084), 10)

    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(self.converter.kilometers_to_miles_conversion(1), 0.621371)
        self.assertAlmostEqual(self.converter.kilometers_to_miles_conversion(0), 0)
        self.assertAlmostEqual(self.converter.kilometers_to_miles_conversion(10), 6.21371)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(self.converter.miles_to_kilometers_conversion(1), 1.60934)
        self.assertAlmostEqual(self.converter.miles_to_kilometers_conversion(0), 0)
        self.assertAlmostEqual(self.converter.miles_to_kilometers_conversion(6.21371), 10)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.meters_to_feet_conversion(5))
    unittest.main(argv=[''], exit=False)