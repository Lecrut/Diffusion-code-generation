import unittest

class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
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
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        meters = value * self.conversion_factors[from_unit]
        result = meters / self.conversion_factors[to_unit]
        return result

class TestDistanceConverter(unittest.TestCase):
    def setUp(self):
        self.converter = DistanceConverter()

    def test_identity_conversion(self):
        self.assertAlmostEqual(self.converter.convert(100, 'meter', 'meter'), 100.0)
        self.assertAlmostEqual(self.converter.convert(5.5, 'mile', 'mile'), 5.5)

    def test_meter_to_kilometer(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'meter', 'kilometer'), 1.0)
        self.assertAlmostEqual(self.converter.convert(1500, 'meter', 'kilometer'), 1.5)

    def test_kilometer_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'kilometer', 'meter'), 1000.0)
        self.assertAlmostEqual(self.converter.convert(0.5, 'kilometer', 'meter'), 500.0)

    def test_meter_to_centimeter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'centimeter'), 100.0)

    def test_centimeter_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(100, 'centimeter', 'meter'), 1.0)

    def test_meter_to_millimeter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'millimeter'), 1000.0)

    def test_millimeter_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1000, 'millimeter', 'meter'), 1.0)

    def test_meter_to_mile(self):
        expected = 1609.344
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'mile'), 1.0 / expected)

    def test_mile_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'meter'), 1609.344)

    def test_meter_to_yard(self):
        expected = 0.9144
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'yard'), 1.0 / expected)

    def test_yard_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'yard', 'meter'), 0.9144)

    def test_meter_to_foot(self):
        expected = 0.3048
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'foot'), 1.0 / expected)

    def test_foot_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'foot', 'meter'), 0.3048)

    def test_meter_to_inch(self):
        expected = 0.0254
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'inch'), 1.0 / expected)

    def test_inch_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'inch', 'meter'), 0.0254)

    def test_meter_to_nautical_mile(self):
        expected = 1852.0
        self.assertAlmostEqual(self.converter.convert(1, 'meter', 'nautical_mile'), 1.0 / expected)

    def test_nautical_mile_to_meter(self):
        self.assertAlmostEqual(self.converter.convert(1, 'nautical_mile', 'meter'), 1852.0)

    def test_cross_conversion_mile_to_km(self):
        mile_in_meters = 1609.344
        expected_km = mile_in_meters / 1000.0
        self.assertAlmostEqual(self.converter.convert(1, 'mile', 'kilometer'), expected_km)

    def test_cross_conversion_foot_to_cm(self):
        foot_in_meters = 0.3048
        expected_cm = foot_in_meters / 0.01
        self.assertAlmostEqual(self.converter.convert(1, 'foot', 'centimeter'), expected_cm)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'invalid_unit', 'meter')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, 'meter', 'invalid_unit')

    def test_zero_value(self):
        self.assertAlmostEqual(self.converter.convert(0, 'meter', 'mile'), 0.0)

    def test_negative_value(self):
        result = self.converter.convert(-100, 'meter', 'kilometer')
        self.assertAlmostEqual(result, -0.1)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'mile', 'kilometer'))
    print(converter.convert(100, 'foot', 'meter'))
    unittest.main()