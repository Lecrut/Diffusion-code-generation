import unittest

class DistanceConverter:
    def __init__(self, distance, unit):
        self.distance = distance
        self.unit = unit.lower()

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        factors = {
            'km': 1.0,
            'm': 1000.0,
            'cm': 100000.0,
            'mm': 1000000.0,
            'mi': 0.621371,
            'yd': 1093.61,
            'ft': 3280.84,
            'in': 39370.1
        }
        if self.unit not in factors:
            raise ValueError(f"Unsupported source unit: {self.unit}")
        if target_unit not in factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        distance_in_meters = self.distance * factors[self.unit] / 1000.0
        
        target_distance = distance_in_meters * 1000.0 / factors[target_unit]
        return target_distance

class TestDistanceConverter(unittest.TestCase):
    def test_km_to_m(self):
        converter = DistanceConverter(1, 'km')
        result = converter.convert('m')
        self.assertAlmostEqual(result, 1000.0, places=5)

    def test_m_to_km(self):
        converter = DistanceConverter(1000, 'm')
        result = converter.convert('km')
        self.assertAlmostEqual(result, 1.0, places=5)

    def test_km_to_mi(self):
        converter = DistanceConverter(1, 'km')
        result = converter.convert('mi')
        self.assertAlmostEqual(result, 0.621371, places=5)

    def test_mi_to_km(self):
        converter = DistanceConverter(1, 'mi')
        result = converter.convert('km')
        self.assertAlmostEqual(result, 1.609344, places=5)

    def test_cm_to_mm(self):
        converter = DistanceConverter(100, 'cm')
        result = converter.convert('mm')
        self.assertAlmostEqual(result, 1000.0, places=5)

    def test_ft_to_cm(self):
        converter = DistanceConverter(1, 'ft')
        result = converter.convert('cm')
        expected = 1 * 30.48
        self.assertAlmostEqual(result, expected, places=5)

    def test_yd_to_m(self):
        converter = DistanceConverter(1, 'yd')
        result = converter.convert('m')
        expected = 0.9144
        self.assertAlmostEqual(result, expected, places=5)

    def test_in_to_cm(self):
        converter = DistanceConverter(1, 'in')
        result = converter.convert('cm')
        expected = 2.54
        self.assertAlmostEqual(result, expected, places=5)

    def test_same_unit(self):
        converter = DistanceConverter(5, 'km')
        result = converter.convert('km')
        self.assertAlmostEqual(result, 5.0, places=5)

    def test_zero_distance(self):
        converter = DistanceConverter(0, 'km')
        result = converter.convert('m')
        self.assertAlmostEqual(result, 0.0, places=5)

    def test_invalid_source_unit(self):
        converter = DistanceConverter(1, 'ly')
        with self.assertRaises(ValueError):
            converter.convert('m')

    def test_invalid_target_unit(self):
        converter = DistanceConverter(1, 'km')
        with self.assertRaises(ValueError):
            converter.convert('parsec')

if __name__ == '__main__':
    converter = DistanceConverter(10, 'km')
    meters = converter.convert('m')
    print(meters)
    
    miles = converter.convert('mi')
    print(miles)
    
    cm = converter.convert('cm')
    print(cm)
    
    unittest.main()