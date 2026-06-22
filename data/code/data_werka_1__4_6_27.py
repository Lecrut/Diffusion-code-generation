import unittest
METER_TO_KILOMETER = 1000.0
KILOMETER_TO_MILE = 1.60934
METER_TO_FOOT = 3.28084

class DistanceConverter:

    def convert(self, distance, from_unit, to_unit):
        if from_unit == to_unit:
            return distance
        if from_unit == 'meter':
            meters = distance
        elif from_unit == 'kilometer':
            meters = distance * METER_TO_KILOMETER
        elif from_unit == 'mile':
            meters = distance * KILOMETER_TO_MILE * METER_TO_KILOMETER
        else:
            raise ValueError(f'Unsupported source unit: {from_unit}')
        if to_unit == 'meter':
            return meters
        elif to_unit == 'kilometer':
            return meters / METER_TO_KILOMETER
        elif to_unit == 'mile':
            return meters / (KILOMETER_TO_MILE * METER_TO_KILOMETER)
        elif to_unit == 'foot':
            return meters * METER_TO_FOOT
        else:
            raise ValueError(f'Unsupported target unit: {to_unit}')

class TestDistanceConverter(unittest.TestCase):

    def setUp(self):
        self.converter = DistanceConverter()

    def test_meter_to_kilometer(self):
        self.assertEqual(self.converter.convert(1000, 'meter', 'kilometer'), 1.0)

    def test_kilometer_to_meter(self):
        self.assertEqual(self.converter.convert(1.0, 'kilometer', 'meter'), 1000)

    def test_mile_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'kilometer'), 1.60934, places=5)

    def test_kilometer_to_mile(self):
        self.assertAlmostEqual(self.converter.convert(1.60934, 'kilometer', 'mile'), 1, places=5)

    def test_meter_to_foot(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'foot'), 3.28084, places=5)

    def test_foot_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(3.28084, 'foot', 'meter'), 1, places=5)

    def test_same_unit(self):
        self.assertEqual(self.converter.convert(5, 'meter', 'meter'), 5)
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1000, 'meter', 'kilometer'))
    print(converter.convert(1.60934, 'kilometer', 'mile'))
    unittest.main(argv=[''], exit=False)