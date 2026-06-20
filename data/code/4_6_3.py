import unittest
import math

class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == 'meter':
            return self.value
        if self.unit == 'kilometer':
            return self.value * 1000.0
        if self.unit == 'centimeter':
            return self.value / 100.0
        if self.unit == 'millimeter':
            return self.value / 1000.0
        if self.unit == 'inch':
            return self.value * 0.0254
        if self.unit == 'foot':
            return self.value * 0.3048
        if self.unit == 'yard':
            return self.value * 0.9144
        if self.unit == 'mile':
            return self.value * 1609.344
        if self.unit == 'nautical_mile':
            return self.value * 1852.0
        raise ValueError(f"Unsupported unit: {self.unit}")

    def convert_to(self, target_unit):
        meters = self.to_meters()
        if target_unit == 'meter':
            return meters
        if target_unit == 'kilometer':
            return meters / 1000.0
        if target_unit == 'centimeter':
            return meters * 100.0
        if target_unit == 'millimeter':
            return meters * 1000.0
        if target_unit == 'inch':
            return meters / 0.0254
        if target_unit == 'foot':
            return meters / 0.3048
        if target_unit == 'yard':
            return meters / 0.9144
        if target_unit == 'mile':
            return meters / 1609.344
        if target_unit == 'nautical_mile':
            return meters / 1852.0
        raise ValueError(f"Unsupported target unit: {target_unit}")

    def get_units(self):
        return ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile', 'nautical_mile']

class TestDistanceConverter(unittest.TestCase):
    def test_meter_to_meters(self):
        converter = DistanceConverter(5.0, 'meter')
        self.assertEqual(converter.to_meters(), 5.0)
        self.assertEqual(converter.convert_to('meter'), 5.0)

    def test_kilometer_to_meters(self):
        converter = DistanceConverter(2.5, 'kilometer')
        self.assertEqual(converter.to_meters(), 2500.0)
        result = converter.convert_to('meter')
        self.assertAlmostEqual(result, 2500.0, places=5)

    def test_centimeter_to_meters(self):
        converter = DistanceConverter(100.0, 'centimeter')
        self.assertEqual(converter.to_meters(), 1.0)
        result = converter.convert_to('meter')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_millimeter_to_meters(self):
        converter = DistanceConverter(500.0, 'millimeter')
        self.assertEqual(converter.to_meters(), 0.5)
        result = converter.convert_to('meter')
        self.assertAlmostEqual(result, 0.5, places=5)

    def test_inch_to_meters(self):
        converter = DistanceConverter(100.0, 'inch')
        result = converter.to_meters()
        self.assertAlmostEqual(result, 2.54, places=5)
        result_converted = converter.convert_to('meter')
        self.assertAlmostEqual(result_converted, 2.54, places=5)

    def test_foot_to_meters(self):
        converter = DistanceConverter(10.0, 'foot')
        result = converter.to_meters()
        self.assertAlmostEqual(result, 3.048, places=5)

    def test_yard_to_meters(self):
        converter = DistanceConverter(10.0, 'yard')
        result = converter.to_meters()
        self.assertAlmostEqual(result, 9.144, places=5)

    def test_mile_to_meters(self):
        converter = DistanceConverter(1.0, 'mile')
        result = converter.to_meters()
        self.assertAlmostEqual(result, 1609.344, places=5)

    def test_nautical_mile_to_meters(self):
        converter = DistanceConverter(1.0, 'nautical_mile')
        result = converter.to_meters()
        self.assertAlmostEqual(result, 1852.0, places=5)

    def test_kilometer_to_miles(self):
        converter = DistanceConverter(1.609344, 'kilometer')
        result = converter.convert_to('mile')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_feet_to_meters(self):
        converter = DistanceConverter(1.0, 'foot')
        result = converter.convert_to('meter')
        self.assertAlmostEqual(result, 0.3048, places=5)

    def test_meters_to_feet(self):
        converter = DistanceConverter(1.0, 'meter')
        result = converter.convert_to('foot')
        expected = 1.0 / 0.3048
        self.assertAlmostEqual(result, expected, places=5)

    def test_meters_to_inches(self):
        converter = DistanceConverter(1.0, 'meter')
        result = converter.convert_to('inch')
        expected = 1.0 / 0.0254
        self.assertAlmostEqual(result, expected, places=5)

    def test_meters_to_nautical_miles(self):
        converter = DistanceConverter(1852.0, 'meter')
        result = converter.convert_to('nautical_mile')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_invalid_unit_source(self):
        converter = DistanceConverter(10.0, 'invalid_unit')
        with self.assertRaises(ValueError):
            converter.to_meters()

    def test_invalid_unit_target(self):
        converter = DistanceConverter(10.0, 'meter')
        with self.assertRaises(ValueError):
            converter.convert_to('invalid_unit')

    def test_zero_value(self):
        converter = DistanceConverter(0.0, 'kilometer')
        self.assertEqual(converter.to_meters(), 0.0)
        self.assertEqual(converter.convert_to('mile'), 0.0)

    def test_get_units(self):
        converter = DistanceConverter(1.0, 'meter')
        units = converter.get_units()
        self.assertIn('kilometer', units)
        self.assertIn('inch', units)
        self.assertEqual(len(units), 9)

if __name__ == '__main__':
    converter = DistanceConverter(1.0, 'kilometer')
    print(f"1.0 km in meters: {converter.to_meters()}")
    print(f"1.0 km in miles: {converter.convert_to('mile')}")
    print(f"1.0 km in feet: {converter.convert_to('foot')}")
    print(f"1.0 mile in meters: {DistanceConverter(1.0, 'mile').to_meters()}")
    print(f"1.0 meter in inches: {DistanceConverter(1.0, 'meter').convert_to('inch')}")
    unittest.main()