import unittest

class DistanceConverter:
    METER_TO_KILOMETER = 0.001
    KILOMETER_TO_METER = 1000
    MILE_TO_KILOMETER = 1.60934
    KILOMETER_TO_MILE = 1 / MILE_TO_KILOMETER
    METER_TO_FOOT = 3.28084
    FOOT_TO_METER = 1 / METER_TO_FOOT
    MILE_TO_FOOT = 5280

    def convert(self, distance, from_unit, to_unit):
        if from_unit == to_unit:
            return distance
        if from_unit == 'meter':
            if to_unit == 'kilometer':
                return distance * self.METER_TO_KILOMETER
            elif to_unit == 'foot':
                return distance * self.METER_TO_FOOT
        elif from_unit == 'kilometer':
            if to_unit == 'meter':
                return distance * self.KILOMETER_TO_METER
            elif to_unit == 'mile':
                return distance * self.KILOMETER_TO_MILE
        elif from_unit == 'mile':
            if to_unit == 'kilometer':
                return distance * self.MILE_TO_KILOMETER
            elif to_unit == 'foot':
                return distance * self.MILE_TO_FOOT
        elif from_unit == 'foot':
            if to_unit == 'meter':
                return distance * self.FOOT_TO_METER
        raise ValueError('Unsupported unit conversion')

class TestDistanceConverter(unittest.TestCase):

    def setUp(self):
        self.converter = DistanceConverter()

    def test_meter_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'meter', 'kilometer'), 1.0)

    def test_kilometer_to_meter(self):
        self.assertEqual(self.converter.convert(1, 'kilometer', 'meter'), 1000)

    def test_mile_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'kilometer'), DistanceConverter.MILE_TO_KILOMETER)

    def test_kilometer_to_mile(self):
        self.assertAlmostEqual(self.converter.convert(DistanceConverter.MILE_TO_KILOMETER, 'kilometer', 'mile'), 1.0)

    def test_meter_to_foot(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'foot'), DistanceConverter.METER_TO_FOOT)

    def test_foot_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(DistanceConverter.METER_TO_FOOT, 'foot', 'meter'), 1.0)

    def test_mile_to_foot(self):
        self.assertEqual(self.converter.convert(1, 'mile', 'foot'), DistanceConverter.MILE_TO_FOOT)

    def test_same_unit(self):
        self.assertEqual(self.converter.convert(50, 'meter', 'meter'), 50)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1000, 'meter', 'kilometer'))
    unittest.main(argv=[''], exit=False)