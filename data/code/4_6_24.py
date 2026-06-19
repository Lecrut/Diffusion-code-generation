import unittest

class DistanceConverter:
    def __init__(self):
        self.meters_to_feet = 3.28084
        self.feet_to_meters = 1 / self.meters_to_feet
        self.meters_to_yards = 1.09361
        self.yards_to_meters = 1 / self.meters_to_yards

    def meters_to_feet_conversion(self, meters):
        return meters * self.meters_to_feet

    def feet_to_meters_conversion(self, feet):
        return feet * self.feet_to_meters

    def meters_to_yards_conversion(self, meters):
        return meters * self.meters_to_yards

    def yards_to_meters_conversion(self, yards):
        return yards * self.yards_to_meters

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
        self.assertAlmostEqual(self.converter.feet_to_meters_conversion(10), 3.048)

    def test_meters_to_yards(self):
        self.assertAlmostEqual(self.converter.meters_to_yards_conversion(1), 1.09361)
        self.assertAlmostEqual(self.converter.meters_to_yards_conversion(0), 0)
        self.assertAlmostEqual(self.converter.meters_to_yards_conversion(10), 10.9361)

    def test_yards_to_meters(self):
        self.assertAlmostEqual(self.converter.yards_to_meters_conversion(1), 0.9144)
        self.assertAlmostEqual(self.converter.yards_to_meters_conversion(0), 0)
        self.assertAlmostEqual(self.converter.yards_to_meters_conversion(10), 9.144)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.meters_to_feet_conversion(5))
    unittest.main(argv=[''], exit=False)