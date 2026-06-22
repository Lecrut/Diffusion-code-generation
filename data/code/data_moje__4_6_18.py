import unittest

class DistanceConverter:
    def __init__(self):
        self.factors = {
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

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors or to_unit not in self.factors:
            raise ValueError("Invalid unit provided")
        base_value = value * self.factors[from_unit]
        return base_value / self.factors[to_unit]

class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()

    def test_meter_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'meter', 'kilometer'), 1.0)

    def test_kilometer_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'kilometer', 'meter'), 1000.0)

    def test_meter_to_mile(self):
        self.assertAlmostEqual(self.converter.convert(1609.344, 'meter', 'mile'), 1.0)

    def test_mile_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'meter'), 1609.344)

    def test_meter_to_foot(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'foot'), 1.0 / 0.3048, places=5)

    def test_foot_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'foot', 'meter'), 0.3048)

    def test_meter_to_inch(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'inch'), 1.0 / 0.0254, places=5)

    def test_inch_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'inch', 'meter'), 0.0254)

    def test_meter_to_centimeter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'centimeter'), 100.0)

    def test_centimeter_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(100, 'centimeter', 'meter'), 1.0)

    def test_meter_to_millimeter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'millimeter'), 1000.0)

    def test_millimeter_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'millimeter', 'meter'), 1.0)

    def test_meter_to_yard(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'yard'), 1.0 / 0.9144, places=5)

    def test_yard_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'yard', 'meter'), 0.9144)

    def test_meter_to_nautical_mile(self):
        self.assertAlmostEqual(self.converter.convert(1852, 'meter', 'nautical_mile'), 1.0)

    def test_nautical_mile_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'nautical_mile', 'meter'), 1852.0)

    def test_mile_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'kilometer'), 1609.344 / 1000.0)

    def test_kilometer_to_mile(self):
        self.assertAlmostEqual(self.converter.convert(1, 'kilometer', 'mile'), 1000.0 / 1609.344, places=5)

    def test_foot_to_inch(self):
        self.assertAlmostEqual(self.converter.convert(1, 'foot', 'inch'), 0.3048 / 0.0254, places=5)

    def test_inch_to_foot(self):
        self.assertAlmostEqual(self.converter.convert(1, 'inch', 'foot'), 0.0254 / 0.3048, places=5)

    def test_zero_value(self):
        self.assertAlmostEqual(self.converter.convert(0, 'meter', 'mile'), 0.0)

    def test_negative_value(self):
        self.assertAlmostEqual(self.converter.convert(-100, 'meter', 'kilometer'), -0.1)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'lightyear', 'meter')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'meter', 'parsec')

    def test_same_unit_conversion(self):
        self.assertAlmostEqual(self.converter.convert(50, 'meter', 'meter'), 50.0)

    def test_large_value_conversion(self):
        self.assertAlmostEqual(self.converter.convert(1e9, 'meter', 'kilometer'), 1e6)

    def test_small_value_conversion(self):
        self.assertAlmostEqual(self.converter.convert(1e-9, 'meter', 'millimeter'), 1e-6)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1000, 'meter', 'kilometer'))
    print(converter.convert(1, 'mile', 'meter'))
    print(converter.convert(100, 'centimeter', 'meter'))
    print(converter.convert(5280, 'foot', 'mile'))
    print(converter.convert(3048, 'millimeter', 'meter'))
    print(converter.convert(1, 'nautical_mile', 'kilometer'))
    print(converter.convert(1, 'yard', 'foot'))
    print(converter.convert(12, 'inch', 'foot'))
    print(converter.convert(0.5, 'kilometer', 'meter'))
    print(converter.convert(100, 'meter', 'inch'))