import unittest

class DistanceConverter:
    def __init__(self):
        self.meters_per_mile = 1609.34
        self.meters_per_yard = 0.9144
        self.yards_per_mile = 1760

    def miles_to_meters(self, miles):
        return miles * self.meters_per_mile

    def meters_to_miles(self, meters):
        return meters / self.meters_per_mile

    def yards_to_meters(self, yards):
        return yards * self.meters_per_yard

    def meters_to_yards(self, meters):
        return meters / self.meters_per_yard

    def miles_to_yards(self, miles):
        return miles * self.yards_per_mile

    def yards_to_miles(self, yards):
        return yards / self.yards_per_mile

class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()

    def test_miles_to_meters(self):
        self.assertAlmostEqual(self.converter.miles_to_meters(1), 1609.34)
        self.assertAlmostEqual(self.converter.miles_to_meters(2.5), 4023.35)

    def test_meters_to_miles(self):
        self.assertAlmostEqual(self.converter.meters_to_miles(1609.34), 1)
        self.assertAlmostEqual(self.converter.meters_to_miles(4023.35), 2.5)

    def test_yards_to_meters(self):
        self.assertAlmostEqual(self.converter.yards_to_meters(1), 0.9144)
        self.assertAlmostEqual(self.converter.yards_to_meters(100), 91.44)

    def test_meters_to_yards(self):
        self.assertAlmostEqual(self.converter.meters_to_yards(0.9144), 1)
        self.assertAlmostEqual(self.converter.meters_to_yards(91.44), 100)

    def test_miles_to_yards(self):
        self.assertEqual(self.converter.miles_to_yards(1), 1760)
        self.assertEqual(self.converter.miles_to_yards(5), 8800)

    def test_yards_to_miles(self):
        self.assertAlmostEqual(self.converter.yards_to_miles(1760), 1)
        self.assertAlmostEqual(self.converter.yards_to_miles(8800), 5)

if __name__ == '__main__':
    converter = DistanceConverter()
    print("1 mile to meters:", converter.miles_to_meters(1))
    print("1609.34 meters to miles:", converter.meters_to_miles(1609.34))
    print("1 yard to meters:", converter.yards_to_meters(1))
    print("0.9144 meters to yards:", converter.meters_to_yards(0.9144))
    print("1 mile to yards:", converter.miles_to_yards(1))
    print("1760 yards to miles:", converter.yards_to_miles(1760))

    unittest.main(argv=[''], exit=False)