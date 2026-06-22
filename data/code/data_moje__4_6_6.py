import unittest
import math

class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
        self.METERS_PER_UNIT = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'mile': 1609.344,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254,
            'nautical_mile': 1852.0
        }

    def to_meters(self):
        if self.unit not in self.METERS_PER_UNIT:
            raise ValueError(f"Unknown unit: {self.unit}")
        return self.value * self.METERS_PER_UNIT[self.unit]

    def convert(self, target_unit):
        if target_unit not in self.METERS_PER_UNIT:
            raise ValueError(f"Unknown target unit: {target_unit}")
        meters = self.to_meters()
        target_factor = self.METERS_PER_UNIT[target_unit]
        return meters / target_factor

    def __str__(self):
        return f"{self.value} {self.unit}"

class TestDistanceConverter(unittest.TestCase):
    def test_init(self):
        dc = DistanceConverter(10, 'meter')
        self.assertEqual(dc.value, 10)
        self.assertEqual(dc.unit, 'meter')

    def test_to_meters_known_units(self):
        self.assertAlmostEqual(DistanceConverter(1, 'meter').to_meters(), 1.0)
        self.assertAlmostEqual(DistanceConverter(1, 'kilometer').to_meters(), 1000.0)
        self.assertAlmostEqual(DistanceConverter(1, 'centimeter').to_meters(), 0.01)
        self.assertAlmostEqual(DistanceConverter(1, 'millimeter').to_meters(), 0.001)
        self.assertAlmostEqual(DistanceConverter(1, 'mile').to_meters(), 1609.344)
        self.assertAlmostEqual(DistanceConverter(1, 'yard').to_meters(), 0.9144)
        self.assertAlmostEqual(DistanceConverter(1, 'foot').to_meters(), 0.3048)
        self.assertAlmostEqual(DistanceConverter(1, 'inch').to_meters(), 0.0254)
        self.assertAlmostEqual(DistanceConverter(1, 'nautical_mile').to_meters(), 1852.0)

    def test_to_meters_unknown_unit(self):
        with self.assertRaises(ValueError):
            DistanceConverter(1, 'lightyear').to_meters()

    def test_convert_same_unit(self):
        dc = DistanceConverter(10, 'kilometer')
        self.assertAlmostEqual(dc.convert('kilometer'), 10.0)

    def test_convert_m_to_km(self):
        dc = DistanceConverter(1000, 'meter')
        self.assertAlmostEqual(dc.convert('kilometer'), 1.0)

    def test_convert_km_to_m(self):
        dc = DistanceConverter(1, 'kilometer')
        self.assertAlmostEqual(dc.convert('meter'), 1000.0)

    def test_convert_km_to_mile(self):
        dc = DistanceConverter(1, 'kilometer')
        expected = 1000.0 / 1609.344
        self.assertAlmostEqual(dc.convert('mile'), expected)

    def test_convert_mile_to_km(self):
        dc = DistanceConverter(1, 'mile')
        expected = 1609.344 / 1000.0
        self.assertAlmostEqual(dc.convert('kilometer'), expected)

    def test_convert_inches_to_cm(self):
        dc = DistanceConverter(1, 'inch')
        expected = 0.0254 / 0.01
        self.assertAlmostEqual(dc.convert('centimeter'), expected)

    def test_convert_cm_to_inches(self):
        dc = DistanceConverter(1, 'centimeter')
        expected = 0.01 / 0.0254
        self.assertAlmostEqual(dc.convert('inch'), expected)

    def test_convert_unknown_target_unit(self):
        dc = DistanceConverter(1, 'meter')
        with self.assertRaises(ValueError):
            dc.convert('furlong')

    def test_convert_case_insensitive(self):
        dc = DistanceConverter(1, 'METER')
        self.assertAlmostEqual(dc.to_meters(), 1.0)
        self.assertAlmostEqual(dc.convert('KM'), 0.001)

    def test_convert_zero_value(self):
        dc = DistanceConverter(0, 'kilometer')
        self.assertAlmostEqual(dc.convert('mile'), 0.0)

    def test_convert_negative_value(self):
        dc = DistanceConverter(-100, 'meter')
        self.assertAlmostEqual(dc.convert('kilometer'), -0.1)

    def test_convert_large_values(self):
        dc = DistanceConverter(1e6, 'kilometer')
        self.assertAlmostEqual(dc.convert('meter'), 1e9)

    def test_convert_small_values(self):
        dc = DistanceConverter(1e-6, 'meter')
        self.assertAlmostEqual(dc.convert('millimeter'), 1e-3)

if __name__ == '__main__':
    converter = DistanceConverter(1, 'kilometer')
    result = converter.convert('mile')
    print(result)
    unittest.main()