class VolumeConverter:
    def __init__(self, volume, unit):
        self.volume = volume
        self.unit = unit.lower()

    def to_liters(self):
        if self.unit == 'liter' or self.unit == 'liters':
            return self.volume
        if self.unit == 'milliliter' or self.unit == 'milliliters':
            return self.volume / 1000.0
        if self.unit == 'gallon' or self.unit == 'gallons':
            return self.volume * 3.78541
        if self.unit == 'quart' or self.unit == 'quarts':
            return self.volume * 0.946353
        if self.unit == 'pint' or self.unit == 'pints':
            return self.volume * 0.473176
        if self.unit == 'cup' or self.unit == 'cups':
            return self.volume * 0.236588
        if self.unit == 'fluid_ounce' or self.unit == 'fluid_ounces':
            return self.volume * 0.0295735
        raise ValueError(f"Unsupported unit: {self.unit}")

    def convert(self, target_unit):
        if self.volume == 0:
            return 0
        liters = self.to_liters()
        if target_unit.lower() == 'liter' or target_unit.lower() == 'liters':
            return liters
        if target_unit.lower() == 'milliliter' or target_unit.lower() == 'milliliters':
            return liters * 1000.0
        if target_unit.lower() == 'gallon' or target_unit.lower() == 'gallons':
            return liters / 3.78541
        if target_unit.lower() == 'quart' or target_unit.lower() == 'quarts':
            return liters / 0.946353
        if target_unit.lower() == 'pint' or target_unit.lower() == 'pints':
            return liters / 0.473176
        if target_unit.lower() == 'cup' or target_unit.lower() == 'cups':
            return liters / 0.236588
        if target_unit.lower() == 'fluid_ounce' or target_unit.lower() == 'fluid_ounces':
            return liters / 0.0295735
        raise ValueError(f"Unsupported target unit: {target_unit}")

import unittest

class TestVolumeConverter(unittest.TestCase):
    def test_zero_volume(self):
        converter = VolumeConverter(0, 'gallon')
        self.assertEqual(converter.to_liters(), 0.0)
        self.assertEqual(converter.convert('liter'), 0.0)
        self.assertEqual(converter.convert('milliliter'), 0.0)

    def test_large_volume(self):
        large_gallons = 1000000
        converter = VolumeConverter(large_gallons, 'gallon')
        expected_liters = large_gallons * 3.78541
        self.assertAlmostEqual(converter.to_liters(), expected_liters, places=2)
        
    def test_gallon_to_liter_conversion(self):
        converter = VolumeConverter(1, 'gallon')
        self.assertAlmostEqual(converter.to_liters(), 3.78541, places=5)
        self.assertAlmostEqual(converter.convert('liter'), 3.78541, places=5)

    def test_milliliter_to_liter_conversion(self):
        converter = VolumeConverter(500, 'milliliter')
        self.assertAlmostEqual(converter.to_liters(), 0.5, places=5)

    def test_liter_to_gallon_conversion(self):
        converter = VolumeConverter(3.78541, 'liter')
        self.assertAlmostEqual(converter.convert('gallon'), 1.0, places=4)

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            converter = VolumeConverter(10, 'invalid_unit')
            converter.to_liters()

    def test_invalid_target_unit(self):
        converter = VolumeConverter(10, 'liter')
        with self.assertRaises(ValueError):
            converter.convert('invalid_unit')

    def test_quart_to_pint_conversion(self):
        converter = VolumeConverter(1, 'quart')
        pints = converter.convert('pint')
        self.assertAlmostEqual(pints, 2.0, places=4)

    def test_cup_to_fluid_ounce(self):
        converter = VolumeConverter(1, 'cup')
        fl_oz = converter.convert('fluid_ounce')
        self.assertAlmostEqual(fl_oz, 8.0, places=2)

if __name__ == '__main__':
    test_large = VolumeConverter(1000000, 'gallon')
    print(f"1,000,000 gallons to liters: {test_large.to_liters()}")
    
    test_zero = VolumeConverter(0, 'liter')
    print(f"0 liters to gallons: {test_zero.convert('gallon')}")
    
    test_small = VolumeConverter(500, 'milliliter')
    print(f"500 milliliters to liters: {test_small.to_liters()}")
    
    test_quart = VolumeConverter(2, 'quart')
    print(f"2 quarts to pints: {test_quart.convert('pint')}")
    
    unittest.main()