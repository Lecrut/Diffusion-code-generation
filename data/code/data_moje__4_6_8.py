import unittest
import math

class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to(self, target_unit):
        if self.unit == target_unit:
            return self.value
        if self.unit == 'meters':
            return self._from_meters(target_unit)
        if self.unit == 'kilometers':
            return self._from_kilometers(target_unit)
        if self.unit == 'miles':
            return self._from_miles(target_unit)
        if self.unit == 'feet':
            return self._from_feet(target_unit)
        raise ValueError(f"Unsupported unit: {self.unit}")

    def _to_meters(self):
        if self.unit == 'meters':
            return self.value
        if self.unit == 'kilometers':
            return self.value * 1000
        if self.unit == 'miles':
            return self.value * 1609.344
        if self.unit == 'feet':
            return self.value / 3.28084
        raise ValueError(f"Unsupported unit: {self.unit}")

    def _from_meters(self, target_unit):
        if target_unit == 'meters':
            return self.value
        if target_unit == 'kilometers':
            return self.value / 1000
        if target_unit == 'miles':
            return self.value / 1609.344
        if target_unit == 'feet':
            return self.value * 3.28084
        raise ValueError(f"Unsupported target unit: {target_unit}")

    def _from_kilometers(self, target_unit):
        meters = self.value * 1000
        return self._from_meters(target_unit)

    def _from_miles(self, target_unit):
        meters = self.value * 1609.344
        return self._from_meters(target_unit)

    def _from_feet(self, target_unit):
        meters = self.value / 3.28084
        return self._from_meters(target_unit)

class TestDistanceConverter(unittest.TestCase):
    def test_same_unit(self):
        converter = DistanceConverter(100, 'meters')
        self.assertAlmostEqual(converter.convert_to('meters'), 100)

        converter = DistanceConverter(5, 'kilometers')
        self.assertAlmostEqual(converter.convert_to('kilometers'), 5)

        converter = DistanceConverter(2, 'miles')
        self.assertAlmostEqual(converter.convert_to('miles'), 2)

        converter = DistanceConverter(10, 'feet')
        self.assertAlmostEqual(converter.convert_to('feet'), 10)

    def test_meters_to_kilometers(self):
        converter = DistanceConverter(1000, 'meters')
        self.assertAlmostEqual(converter.convert_to('kilometers'), 1)

    def test_meters_to_miles(self):
        converter = DistanceConverter(1609.344, 'meters')
        self.assertAlmostEqual(converter.convert_to('miles'), 1)

    def test_meters_to_feet(self):
        converter = DistanceConverter(1, 'meters')
        self.assertAlmostEqual(converter.convert_to('feet'), 3.28084, places=5)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter(2.5, 'kilometers')
        self.assertAlmostEqual(converter.convert_to('meters'), 2500)

    def test_kilometers_to_miles(self):
        converter = DistanceConverter(1, 'kilometers')
        self.assertAlmostEqual(converter.convert_to('miles'), 0.621371, places=6)

    def test_miles_to_meters(self):
        converter = DistanceConverter(1, 'miles')
        self.assertAlmostEqual(converter.convert_to('meters'), 1609.344)

    def test_miles_to_kilometers(self):
        converter = DistanceConverter(1, 'miles')
        self.assertAlmostEqual(converter.convert_to('kilometers'), 1.609344)

    def test_miles_to_feet(self):
        converter = DistanceConverter(1, 'miles')
        self.assertAlmostEqual(converter.convert_to('feet'), 5280)

    def test_feet_to_meters(self):
        converter = DistanceConverter(3.28084, 'feet')
        self.assertAlmostEqual(converter.convert_to('meters'), 1, places=5)

    def test_feet_to_kilometers(self):
        converter = DistanceConverter(3280.84, 'feet')
        self.assertAlmostEqual(converter.convert_to('kilometers'), 1, places=5)

    def test_feet_to_miles(self):
        converter = DistanceConverter(5280, 'feet')
        self.assertAlmostEqual(converter.convert_to('miles'), 1)

    def test_chain_conversion(self):
        converter = DistanceConverter(1, 'miles')
        result = converter.convert_to('kilometers')
        converter2 = DistanceConverter(result, 'kilometers')
        final = converter2.convert_to('meters')
        self.assertAlmostEqual(final, 1609.344)

    def test_invalid_unit_raise(self):
        with self.assertRaises(ValueError):
            DistanceConverter(10, 'invalid_unit').convert_to('meters')

        with self.assertRaises(ValueError):
            DistanceConverter(10, 'meters').convert_to('invalid_target')

if __name__ == '__main__':
    converter = DistanceConverter(1.5, 'miles')
    result_meters = converter.convert_to('meters')
    result_km = converter.convert_to('kilometers')
    print(f"{1.5} miles is {result_meters} meters")
    print(f"{1.5} miles is {result_km} kilometers")
    
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestDistanceConverter)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)