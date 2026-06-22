import unittest
import math
from decimal import Decimal, InvalidOperation, getcontext
getcontext().prec = 50

def convert_volume(value, from_unit, to_unit):
    if value < 0:
        raise ValueError('Volume value cannot be negative.')
    to_liters = {'liter': 1.0, 'litre': 1.0, 'milliliter': 0.001, 'millilitre': 0.001, 'gallon': 3.785411784, 'quart': 0.946352946, 'pint': 0.473176473, 'cup': 0.2365882365, 'tablespoon': 0.014786764781, 'teaspoon': 0.004928921594, 'cubic_meter': 1000.0, 'cubic_centimeter': 0.001, 'cubic_inch': 0.016387064, 'cubic_foot': 28.316846592}
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in to_liters:
        raise ValueError(f'Unsupported source unit: {from_unit}')
    if to_unit_lower not in to_liters:
        raise ValueError(f'Unsupported target unit: {to_unit}')
    if value == 0:
        return 0.0
    value_in_liters = value * to_liters[from_unit_lower]
    converted_value = value_in_liters / to_liters[to_unit_lower]
    if math.isinf(converted_value):
        raise OverflowError('Conversion resulted in an overflow.')
    return converted_value

class TestVolumeConversion(unittest.TestCase):

    def test_zero_volume(self):
        self.assertAlmostEqual(convert_volume(0, 'liter', 'gallon'), 0.0)
        self.assertAlmostEqual(convert_volume(0, 'gallon', 'liter'), 0.0)
        self.assertAlmostEqual(convert_volume(0, 'cubic_meter', 'milliliter'), 0.0)

    def test_identity_conversion(self):
        self.assertAlmostEqual(convert_volume(5.0, 'liter', 'liter'), 5.0)
        self.assertAlmostEqual(convert_volume(10.0, 'gallon', 'gallon'), 10.0)
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_meter', 'cubic_meter'), 1.0)

    def test_liters_to_milliliters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'liter', 'milliliter'), 1000.0)
        self.assertAlmostEqual(convert_volume(2.5, 'liter', 'milliliter'), 2500.0)

    def test_milliliters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1000.0, 'milliliter', 'liter'), 1.0)
        self.assertAlmostEqual(convert_volume(500.0, 'milliliter', 'liter'), 0.5)

    def test_gallons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'gallon', 'liter'), 3.785411784)
        self.assertAlmostEqual(convert_volume(0.5, 'gallon', 'liter'), 1.892705892)

    def test_liters_to_gallons(self):
        result = convert_volume(1.0, 'liter', 'gallon')
        self.assertAlmostEqual(result, 0.264172052, places=8)

    def test_quarts_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'quart', 'liter'), 0.946352946)

    def test_pints_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'pint', 'liter'), 0.473176473)

    def test_cups_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cup', 'liter'), 0.2365882365)

    def test_tablespoons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'tablespoon', 'liter'), 0.014786764781)

    def test_teaspoons_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'teaspoon', 'liter'), 0.004928921594)

    def test_cubic_meters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_meter', 'liter'), 1000.0)
        self.assertAlmostEqual(convert_volume(2.0, 'cubic_meter', 'liter'), 2000.0)

    def test_liters_to_cubic_meters(self):
        self.assertAlmostEqual(convert_volume(1000.0, 'liter', 'cubic_meter'), 1.0)

    def test_cubic_centimeters_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_centimeter', 'liter'), 0.001)

    def test_cubic_inches_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_inch', 'liter'), 0.016387064)

    def test_cubic_feet_to_liters(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_foot', 'liter'), 28.316846592)

    def test_large_volume_gallons_to_liters(self):
        expected = 1000000.0 * 3.785411784
        self.assertAlmostEqual(convert_volume(1000000.0, 'gallon', 'liter'), expected)

    def test_large_volume_liters_to_milliliters(self):
        expected = 1000000.0 * 1000.0
        self.assertAlmostEqual(convert_volume(1000000.0, 'liter', 'milliliter'), expected)

    def test_small_volume_milliliters_to_liters(self):
        expected = 1e-06 * 0.001
        self.assertAlmostEqual(convert_volume(1e-06, 'milliliter', 'liter'), expected)

    def test_negative_value_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(-1.0, 'liter', 'gallon')

    def test_invalid_from_unit_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(1.0, 'barrel', 'liter')

    def test_invalid_to_unit_raises_error(self):
        with self.assertRaises(ValueError):
            convert_volume(1.0, 'liter', 'gallons')

    def test_case_insensitive_units(self):
        self.assertAlmostEqual(convert_volume(1.0, 'Liter', 'Milliliter'), 1000.0)
        self.assertAlmostEqual(convert_volume(1.0, 'LITER', 'MILLILITER'), 1000.0)
        self.assertAlmostEqual(convert_volume(1.0, 'Gallon', 'Liter'), 3.785411784)
        self.assertAlmostEqual(convert_volume(1.0, 'GALLON', 'LITER'), 3.785411784)

    def test_cross_unit_conversion(self):
        expected_cups = 16.0
        self.assertAlmostEqual(convert_volume(1.0, 'gallon', 'cup'), expected_cups)

    def test_cubic_inch_to_cubic_foot(self):
        self.assertAlmostEqual(convert_volume(1.0, 'cubic_foot', 'cubic_inch'), 1728.0)

    def test_cubic_foot_to_cubic_inch(self):
        result = convert_volume(1.0, 'cubic_inch', 'cubic_foot')
        self.assertAlmostEqual(result, 1.0 / 1728.0, places=10)
if __name__ == '__main__':
    print(convert_volume(1, 'liter', 'gallon'))
    print(convert_volume(0, 'liter', 'gallon'))
    print(convert_volume(1000, 'milliliter', 'liter'))
    print(convert_volume(1, 'cubic_meter', 'liter'))