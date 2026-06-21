import unittest
import math

class VolumeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()

    def to_liters(self):
        if self.value < 0:
            raise ValueError("Volume cannot be negative")
        conversions = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.78541,
            'quart': 0.946353,
            'pint': 0.473176,
            'cup': 0.236588,
            'cubic_meter': 1000.0,
            'cubic_foot': 28.3168,
            'fluid_ounce': 0.0295735,
            'tablespoon': 0.0147868,
            'teaspoon': 0.00492892,
            'imperial_gallon': 4.54609,
            'imperial_quart': 1.13652,
            'imperial_pint': 0.568261,
            'imperial_cup': 0.284131,
            'imperial_fluid_ounce': 0.0284131
        }
        if self.unit not in conversions:
            raise ValueError(f"Unsupported unit: {self.unit}")
        return self.value * conversions[self.unit]

    def to_unit(self, target_unit):
        liters = self.to_liters()
        if target_unit == 'liter':
            return liters
        conversions = {
            'milliliter': 1000.0,
            'gallon': 1.0 / 3.78541,
            'quart': 1.0 / 0.946353,
            'pint': 1.0 / 0.473176,
            'cup': 1.0 / 0.236588,
            'cubic_meter': 0.001,
            'cubic_foot': 1.0 / 28.3168,
            'fluid_ounce': 1.0 / 0.0295735,
            'tablespoon': 1.0 / 0.0147868,
            'teaspoon': 1.0 / 0.00492892,
            'imperial_gallon': 1.0 / 4.54609,
            'imperial_quart': 1.0 / 1.13652,
            'imperial_pint': 1.0 / 0.568261,
            'imperial_cup': 1.0 / 0.284131,
            'imperial_fluid_ounce': 1.0 / 0.0284131
        }
        if target_unit.lower() not in conversions:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        return liters * conversions[target_unit.lower()]

class TestVolumeConverter(unittest.TestCase):
    def test_zero_volume(self):
        converter = VolumeConverter(0, 'liter')
        self.assertEqual(converter.to_liters(), 0.0)

    def test_liter_to_milliliter(self):
        converter = VolumeConverter(1, 'liter')
        self.assertAlmostEqual(converter.to_liters(), 1.0)
        self.assertAlmostEqual(converter.to_unit('milliliter'), 1000.0)

    def test_gallon_to_liter(self):
        converter = VolumeConverter(1, 'gallon')
        self.assertAlmostEqual(converter.to_liters(), 3.78541, places=5)

    def test_large_number_conversion(self):
        converter = VolumeConverter(1000000, 'gallon')
        expected = 3785410.0
        result = converter.to_liters()
        self.assertAlmostEqual(result, expected, delta=1.0)

    def test_negative_volume_raises_error(self):
        with self.assertRaises(ValueError):
            VolumeConverter(-5, 'liter')

    def test_invalid_unit_raises_error(self):
        with self.assertRaises(ValueError):
            VolumeConverter(5, 'invalid_unit')

    def test_imperial_gallon_conversion(self):
        converter = VolumeConverter(1, 'imperial_gallon')
        self.assertAlmostEqual(converter.to_liters(), 4.54609, places=5)

    def test_cubic_meter_conversion(self):
        converter = VolumeConverter(1, 'cubic_meter')
        self.assertAlmostEqual(converter.to_liters(), 1000.0)

    def test_cubic_foot_conversion(self):
        converter = VolumeConverter(1, 'cubic_foot')
        self.assertAlmostEqual(converter.to_liters(), 28.3168, places=4)

    def test_round_trip_conversion(self):
        converter = VolumeConverter(50, 'pint')
        liters = converter.to_liters()
        back_to_pints = VolumeConverter(liters, 'liter').to_unit('pint')
        self.assertAlmostEqual(back_to_pints, 50.0, places=3)

    def test_small_fractional_volume(self):
        converter = VolumeConverter(0.000001, 'milliliter')
        result = converter.to_liters()
        self.assertAlmostEqual(result, 1e-9)

    def test_teaspoon_to_fluid_ounce(self):
        converter = VolumeConverter(3, 'teaspoon')
        result = converter.to_unit('fluid_ounce')
        self.assertAlmostEqual(result, 0.5, places=5)

if __name__ == '__main__':
    sample_liter_to_gallon = VolumeConverter(100, 'liter').to_unit('gallon')
    print(f"100 liters to gallons: {sample_liter_to_gallon}")
    
    sample_zero_milliliter = VolumeConverter(0, 'milliliter').to_liters()
    print(f"0 milliliters to liters: {sample_zero_milliliter}")
    
    sample_large_cubic_feet = VolumeConverter(50000, 'cubic_foot').to_liters()
    print(f"50000 cubic feet to liters: {sample_large_cubic_feet}")
    
    sample_imperial_to_metric = VolumeConverter(10, 'imperial_gallon').to_liters()
    print(f"10 imperial gallons to liters: {sample_imperial_to_metric}")
    
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestVolumeConverter)
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(test_suite)