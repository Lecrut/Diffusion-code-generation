import unittest
import math

class DistanceConverter:
    METERS_PER_KILOMETER = 1000.0
    METERS_PER_MILE = 1609.344
    METERS_PER_FOOT = 0.3048
    METERS_PER_INCH = 0.0254
    METERS_PER_CENTIMETER = 0.01
    METERS_PER_METER = 1.0

    @staticmethod
    def to_meters(value, unit):
        unit_lower = unit.lower()
        if unit_lower == 'meter':
            return value * DistanceConverter.METERS_PER_METER
        elif unit_lower == 'kilometer':
            return value * DistanceConverter.METERS_PER_KILOMETER
        elif unit_lower == 'mile':
            return value * DistanceConverter.METERS_PER_MILE
        elif unit_lower == 'foot':
            return value * DistanceConverter.METERS_PER_FOOT
        elif unit_lower == 'inch':
            return value * DistanceConverter.METERS_PER_INCH
        elif unit_lower == 'centimeter':
            return value * DistanceConverter.METERS_PER_CENTIMETER
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    @staticmethod
    def from_meters(value, unit):
        unit_lower = unit.lower()
        if unit_lower == 'meter':
            return value / DistanceConverter.METERS_PER_METER
        elif unit_lower == 'kilometer':
            return value / DistanceConverter.METERS_PER_KILOMETER
        elif unit_lower == 'mile':
            return value / DistanceConverter.METERS_PER_MILE
        elif unit_lower == 'foot':
            return value / DistanceConverter.METERS_PER_FOOT
        elif unit_lower == 'inch':
            return value / DistanceConverter.METERS_PER_INCH
        elif unit_lower == 'centimeter':
            return value / DistanceConverter.METERS_PER_CENTIMETER
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    @staticmethod
    def convert(value, from_unit, to_unit):
        meters = DistanceConverter.to_meters(value, from_unit)
        return DistanceConverter.from_meters(meters, to_unit)

class TestDistanceConverter(unittest.TestCase):
    def test_kilometer_to_meter(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'kilometer', 'meter'), 1000.0)

    def test_meter_to_kilometer(self):
        self.assertAlmostEqual(DistanceConverter.convert(1000, 'meter', 'kilometer'), 1.0)

    def test_mile_to_meter(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'mile', 'meter'), 1609.344)

    def test_meter_to_mile(self):
        self.assertAlmostEqual(DistanceConverter.convert(1609.344, 'meter', 'mile'), 1.0)

    def test_foot_to_meter(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'foot', 'meter'), 0.3048)

    def test_meter_to_foot(self):
        self.assertAlmostEqual(DistanceConverter.convert(0.3048, 'meter', 'foot'), 1.0)

    def test_inch_to_meter(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'inch', 'meter'), 0.0254)

    def test_meter_to_inch(self):
        self.assertAlmostEqual(DistanceConverter.convert(0.0254, 'meter', 'inch'), 1.0)

    def test_centimeter_to_meter(self):
        self.assertAlmostEqual(DistanceConverter.convert(100, 'centimeter', 'meter'), 1.0)

    def test_meter_to_centimeter(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'meter', 'centimeter'), 100.0)

    def test_mile_to_kilometer(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'mile', 'kilometer'), 1.609344)

    def test_kilometer_to_mile(self):
        self.assertAlmostEqual(DistanceConverter.convert(1.609344, 'kilometer', 'mile'), 1.0)

    def test_foot_to_inch(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'foot', 'inch'), 12.0)

    def test_inch_to_foot(self):
        self.assertAlmostEqual(DistanceConverter.convert(12, 'inch', 'foot'), 1.0)

    def test_case_insensitivity(self):
        self.assertAlmostEqual(DistanceConverter.convert(1, 'KILOMETER', 'Meter'), 1000.0)
        self.assertAlmostEqual(DistanceConverter.convert(1, 'MiLe', 'FOOT'), 5280.0)

    def test_zero_value(self):
        self.assertEqual(DistanceConverter.convert(0, 'mile', 'meter'), 0.0)
        self.assertEqual(DistanceConverter.convert(0, 'centimeter', 'inch'), 0.0)

    def test_negative_value(self):
        self.assertAlmostEqual(DistanceConverter.convert(-5, 'kilometer', 'meter'), -5000.0)

    def test_invalid_unit_to_meters(self):
        with self.assertRaises(ValueError):
            DistanceConverter.to_meters(10, 'yard')

    def test_invalid_unit_from_meters(self):
        with self.assertRaises(ValueError):
            DistanceConverter.from_meters(10, 'lightyear')

    def test_invalid_unit_convert(self):
        with self.assertRaises(ValueError):
            DistanceConverter.convert(10, 'parsec', 'meter')

    def test_miles_to_feet(self):
        self.assertAlmostEqual(DistanceConverter.convert(2, 'mile', 'foot'), 10560.0)

    def test_inches_to_miles(self):
        self.assertAlmostEqual(DistanceConverter.convert(63360, 'inch', 'mile'), 1.0)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'kilometer', 'mile'))
    print(converter.convert(5000, 'meter', 'foot'))
    print(converter.convert(12, 'inch', 'centimeter'))
    print(converter.convert(1, 'mile', 'kilometer'))
    unittest.main(verbosity=2)