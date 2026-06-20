import unittest

class DistanceConverter:
    METERS_PER_KILOMETER = 1000
    METERS_PER_MILE = 1609.344
    METERS_PER_FOOT = 0.3048
    METERS_PER_INCH = 0.0254

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.lower()
        if self.unit not in ['meter', 'kilometer', 'mile', 'foot', 'inch']:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def _to_meters(self):
        if self.unit == 'meter':
            return self.value
        if self.unit == 'kilometer':
            return self.value * self.METERS_PER_KILOMETER
        if self.unit == 'mile':
            return self.value * self.METERS_PER_MILE
        if self.unit == 'foot':
            return self.value * self.METERS_PER_FOOT
        if self.unit == 'inch':
            return self.value * self.METERS_PER_INCH
        raise ValueError(f"Cannot convert {self.unit} to meters")

    def convert_to(self, target_unit):
        if target_unit.lower() not in ['meter', 'kilometer', 'mile', 'foot', 'inch']:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        if self.unit == target_unit.lower():
            return self.value
        meters = self._to_meters()
        if target_unit.lower() == 'meter':
            return meters
        if target_unit.lower() == 'kilometer':
            return meters / self.METERS_PER_KILOMETER
        if target_unit.lower() == 'mile':
            return meters / self.METERS_PER_MILE
        if target_unit.lower() == 'foot':
            return meters / self.METERS_PER_FOOT
        if target_unit.lower() == 'inch':
            return meters / self.METERS_PER_INCH
        raise ValueError(f"Cannot convert meters to {target_unit}")

class TestDistanceConverter(unittest.TestCase):
    def test_kilometer_to_meter(self):
        converter = DistanceConverter(1, 'kilometer')
        self.assertAlmostEqual(converter.convert_to('meter'), 1000.0)

    def test_meter_to_kilometer(self):
        converter = DistanceConverter(500, 'meter')
        self.assertAlmostEqual(converter.convert_to('kilometer'), 0.5)

    def test_mile_to_meter(self):
        converter = DistanceConverter(1, 'mile')
        self.assertAlmostEqual(converter.convert_to('meter'), 1609.344)

    def test_meter_to_mile(self):
        converter = DistanceConverter(1609.344, 'meter')
        self.assertAlmostEqual(converter.convert_to('mile'), 1.0)

    def test_foot_to_meter(self):
        converter = DistanceConverter(1, 'foot')
        self.assertAlmostEqual(converter.convert_to('meter'), 0.3048)

    def test_meter_to_foot(self):
        converter = DistanceConverter(0.3048, 'meter')
        self.assertAlmostEqual(converter.convert_to('foot'), 1.0)

    def test_inch_to_meter(self):
        converter = DistanceConverter(1, 'inch')
        self.assertAlmostEqual(converter.convert_to('meter'), 0.0254)

    def test_meter_to_inch(self):
        converter = DistanceConverter(0.0254, 'meter')
        self.assertAlmostEqual(converter.convert_to('inch'), 1.0)

    def test_mile_to_kilometer(self):
        converter = DistanceConverter(1, 'mile')
        self.assertAlmostEqual(converter.convert_to('kilometer'), 1.609344)

    def test_kilometer_to_mile(self):
        converter = DistanceConverter(1.609344, 'kilometer')
        self.assertAlmostEqual(converter.convert_to('mile'), 1.0)

    def test_foot_to_mile(self):
        converter = DistanceConverter(5280, 'foot')
        self.assertAlmostEqual(converter.convert_to('mile'), 1.0)

    def test_mile_to_foot(self):
        converter = DistanceConverter(1, 'mile')
        self.assertAlmostEqual(converter.convert_to('foot'), 5280.0)

    def test_inch_to_foot(self):
        converter = DistanceConverter(12, 'inch')
        self.assertAlmostEqual(converter.convert_to('foot'), 1.0)

    def test_foot_to_inch(self):
        converter = DistanceConverter(1, 'foot')
        self.assertAlmostEqual(converter.convert_to('inch'), 12.0)

    def test_invalid_unit_init(self):
        with self.assertRaises(ValueError):
            DistanceConverter(1, 'lightyear')

    def test_invalid_target_unit(self):
        converter = DistanceConverter(1, 'meter')
        with self.assertRaises(ValueError):
            converter.convert_to('lightyear')

    def test_same_unit_conversion(self):
        converter = DistanceConverter(10, 'meter')
        self.assertEqual(converter.convert_to('meter'), 10.0)

if __name__ == '__main__':
    converter1 = DistanceConverter(10, 'kilometer')
    print(converter1.convert_to('meter'))
    converter2 = DistanceConverter(1609.344, 'meter')
    print(converter2.convert_to('mile'))
    converter3 = DistanceConverter(100, 'foot')
    print(converter3.convert_to('meter'))
    unittest.main(exit=False)