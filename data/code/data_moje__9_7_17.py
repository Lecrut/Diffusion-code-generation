import unittest

def convert_volume(value, from_unit, to_unit):
    units = {
        'ml': 1.0,
        'l': 1000.0,
        'us_fl_oz': 29.5735,
        'us_cup': 236.588,
        'us_gal': 3785.41,
        'uk_fl_oz': 28.4131,
        'uk_pint': 568.261
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit")
    
    if value < 0:
        raise ValueError("Volume cannot be negative")
    
    value_in_ml = value * units[from_unit]
    return value_in_ml / units[to_unit]

class TestVolumeConversion(unittest.TestCase):
    def test_liters_to_ml(self):
        self.assertEqual(convert_volume(1, 'l', 'ml'), 1000.0)
    
    def test_ml_to_liters(self):
        self.assertAlmostEqual(convert_volume(500, 'ml', 'l'), 0.5, places=2)
    
    def test_zero_volume(self):
        self.assertEqual(convert_volume(0, 'l', 'ml'), 0.0)
    
    def test_large_number(self):
        self.assertEqual(convert_volume(1000000, 'l', 'ml'), 1000000000.0)
    
    def test_gallon_to_fl_oz(self):
        self.assertAlmostEqual(convert_volume(1, 'us_gal', 'us_fl_oz'), 128.0, places=2)
    
    def test_cup_to_ml(self):
        self.assertAlmostEqual(convert_volume(2, 'us_cup', 'ml'), 473.176, places=2)
    
    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'gallon', 'ml')
    
    def test_negative_volume(self):
        with self.assertRaises(ValueError):
            convert_volume(-5, 'l', 'ml')

def get_converted_volume():
    return convert_volume(5, 'l', 'us_fl_oz')

def get_large_conversion():
    return convert_volume(100000, 'us_gal', 'ml')

def get_zero_conversion():
    return convert_volume(0, 'us_cup', 'l')

if __name__ == '__main__':
    result1 = get_converted_volume()
    print(result1)
    result2 = get_large_conversion()
    print(result2)
    result3 = get_zero_conversion()
    print(result3)
    unittest.main(argv=[''], exit=False)