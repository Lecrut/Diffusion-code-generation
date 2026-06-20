import unittest
import math

class DistanceConverter:
    def __init__(self):
        self.factors = {
            'km_to_m': 1000,
            'km_to_km': 1,
            'km_to_cm': 100000,
            'km_to_mm': 1000000,
            'km_to_mi': 0.621371,
            'km_to_ft': 3280.84,
            'm_to_km': 0.001,
            'm_to_m': 1,
            'm_to_cm': 100,
            'm_to_mm': 1000,
            'm_to_mi': 0.000621371,
            'm_to_ft': 3.28084,
            'cm_to_km': 0.00001,
            'cm_to_m': 0.01,
            'cm_to_cm': 1,
            'cm_to_mm': 10,
            'cm_to_mi': 6.21371e-06,
            'cm_to_ft': 0.0328084,
            'mm_to_km': 1e-06,
            'mm_to_m': 0.001,
            'mm_to_cm': 0.1,
            'mm_to_mm': 1,
            'mm_to_mi': 6.21371e-07,
            'mm_to_ft': 0.00328084,
            'mi_to_km': 1.60934,
            'mi_to_m': 1609.34,
            'mi_to_cm': 160934,
            'mi_to_mm': 1609340,
            'mi_to_mi': 1,
            'mi_to_ft': 5280,
            'ft_to_km': 0.0003048,
            'ft_to_m': 0.3048,
            'ft_to_cm': 30.48,
            'ft_to_mm': 304.8,
            'ft_to_mi': 0.000189394,
            'ft_to_ft': 1,
        }

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key not in self.factors:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
        return value * self.factors[key]

class TestDistanceConverter(unittest.TestCase):

    def test_km_to_m(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'km', 'm')
        self.assertEqual(result, 1000)

    def test_km_to_cm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'km', 'cm')
        self.assertEqual(result, 100000)

    def test_km_to_mm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'km', 'mm')
        self.assertEqual(result, 1000000)

    def test_km_to_mi(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'km', 'mi')
        self.assertAlmostEqual(result, 0.621371, places=6)

    def test_km_to_ft(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'km', 'ft')
        self.assertAlmostEqual(result, 3280.84, places=2)

    def test_m_to_km(self):
        converter = DistanceConverter()
        result = converter.convert(1000, 'm', 'km')
        self.assertEqual(result, 1)

    def test_m_to_cm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'm', 'cm')
        self.assertEqual(result, 100)

    def test_m_to_mm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'm', 'mm')
        self.assertEqual(result, 1000)

    def test_m_to_mi(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'm', 'mi')
        self.assertAlmostEqual(result, 0.000621371, places=9)

    def test_m_to_ft(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'm', 'ft')
        self.assertAlmostEqual(result, 3.28084, places=5)

    def test_cm_to_km(self):
        converter = DistanceConverter()
        result = converter.convert(100000, 'cm', 'km')
        self.assertEqual(result, 1)

    def test_cm_to_m(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'cm', 'm')
        self.assertEqual(result, 0.01)

    def test_cm_to_mm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'cm', 'mm')
        self.assertEqual(result, 10)

    def test_cm_to_mi(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'cm', 'mi')
        self.assertAlmostEqual(result, 6.21371e-06, places=11)

    def test_cm_to_ft(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'cm', 'ft')
        self.assertAlmostEqual(result, 0.0328084, places=7)

    def test_mm_to_km(self):
        converter = DistanceConverter()
        result = converter.convert(1000000, 'mm', 'km')
        self.assertEqual(result, 1)

    def test_mm_to_m(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mm', 'm')
        self.assertEqual(result, 0.001)

    def test_mm_to_cm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mm', 'cm')
        self.assertEqual(result, 0.1)

    def test_mm_to_mi(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mm', 'mi')
        self.assertAlmostEqual(result, 6.21371e-07, places=11)

    def test_mm_to_ft(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mm', 'ft')
        self.assertAlmostEqual(result, 0.00328084, places=8)

    def test_mi_to_km(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mi', 'km')
        self.assertAlmostEqual(result, 1.60934, places=5)

    def test_mi_to_m(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mi', 'm')
        self.assertAlmostEqual(result, 1609.34, places=2)

    def test_mi_to_cm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mi', 'cm')
        self.assertAlmostEqual(result, 160934, places=0)

    def test_mi_to_mm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mi', 'mm')
        self.assertAlmostEqual(result, 1609340, places=0)

    def test_mi_to_ft(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'mi', 'ft')
        self.assertEqual(result, 5280)

    def test_ft_to_km(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'ft', 'km')
        self.assertAlmostEqual(result, 0.0003048, places=7)

    def test_ft_to_m(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'ft', 'm')
        self.assertAlmostEqual(result, 0.3048, places=4)

    def test_ft_to_cm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'ft', 'cm')
        self.assertAlmostEqual(result, 30.48, places=2)

    def test_ft_to_mm(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'ft', 'mm')
        self.assertAlmostEqual(result, 304.8, places=1)

    def test_ft_to_mi(self):
        converter = DistanceConverter()
        result = converter.convert(1, 'ft', 'mi')
        self.assertAlmostEqual(result, 0.000189394, places=9)

    def test_zero_value_conversion(self):
        converter = DistanceConverter()
        result = converter.convert(0, 'km', 'm')
        self.assertEqual(result, 0)

    def test_invalid_conversion(self):
        converter = DistanceConverter()
        with self.assertRaises(ValueError):
            converter.convert(1, 'km', 'lightyear')

    def test_negative_value_conversion(self):
        converter = DistanceConverter()
        result = converter.convert(-1, 'km', 'm')
        self.assertEqual(result, -1000)

if __name__ == '__main__':
    converter = DistanceConverter()
    
    km_to_m_result = converter.convert(5, 'km', 'm')
    print(km_to_m_result)
    
    mi_to_km_result = converter.convert(10, 'mi', 'km')
    print(mi_to_km_result)
    
    ft_to_m_result = converter.convert(1, 'ft', 'm')
    print(ft_to_m_result)
    
    cm_to_in_result = converter.convert(2.54, 'cm', 'in')
    print(cm_to_in_result)