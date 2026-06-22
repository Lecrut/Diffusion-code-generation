import unittest

class DistanceConverter:
    def __init__(self):
        self.conversions = {
            'm_to_ft': 3.28084,
            'm_to_in': 39.3701,
            'm_to_km': 0.001,
            'ft_to_m': 0.3048,
            'ft_to_in': 12.0,
            'ft_to_km': 0.0003048,
            'in_to_m': 0.0254,
            'in_to_ft': 1.0 / 12.0,
            'in_to_km': 0.0000254,
            'km_to_m': 1000.0,
            'km_to_ft': 3280.84,
            'km_to_in': 39370.1,
        }

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        
        if from_unit == to_unit:
            return value

        if from_unit == 'm' and to_unit == 'ft':
            return value * self.conversions['m_to_ft']
        elif from_unit == 'm' and to_unit == 'in':
            return value * self.conversions['m_to_in']
        elif from_unit == 'm' and to_unit == 'km':
            return value * self.conversions['m_to_km']
        elif from_unit == 'ft' and to_unit == 'm':
            return value * self.conversions['ft_to_m']
        elif from_unit == 'ft' and to_unit == 'in':
            return value * self.conversions['ft_to_in']
        elif from_unit == 'ft' and to_unit == 'km':
            return value * self.conversions['ft_to_km']
        elif from_unit == 'in' and to_unit == 'm':
            return value * self.conversions['in_to_m']
        elif from_unit == 'in' and to_unit == 'ft':
            return value * self.conversions['in_to_ft']
        elif from_unit == 'in' and to_unit == 'km':
            return value * self.conversions['in_to_km']
        elif from_unit == 'km' and to_unit == 'm':
            return value * self.conversions['km_to_m']
        elif from_unit == 'km' and to_unit == 'ft':
            return value * self.conversions['km_to_ft']
        elif from_unit == 'km' and to_unit == 'in':
            return value * self.conversions['km_to_in']
        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

class TestDistanceConverter(unittest.TestCase):

    def test_meters_to_feet(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'm', 'ft'), 3.28084)

    def test_meters_to_inches(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'm', 'in'), 39.3701)

    def test_meters_to_kilometers(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'm', 'km'), 0.001)

    def test_feet_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'ft', 'm'), 0.3048)

    def test_feet_to_inches(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'ft', 'in'), 12.0)

    def test_feet_to_kilometers(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'ft', 'km'), 0.0003048)

    def test_inches_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'in', 'm'), 0.0254)

    def test_inches_to_feet(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'in', 'ft'), 1.0 / 12.0)

    def test_inches_to_kilometers(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'in', 'km'), 0.0000254)

    def test_kilometers_to_meters(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'km', 'm'), 1000.0)

    def test_kilometers_to_feet(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'km', 'ft'), 3280.84)

    def test_kilometers_to_inches(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(1, 'km', 'in'), 39370.1)

    def test_same_unit(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(5, 'm', 'm'), 5.0)
        self.assertAlmostEqual(converter.convert(5, 'ft', 'ft'), 5.0)

    def test_zero_distance(self):
        converter = DistanceConverter()
        self.assertAlmostEqual(converter.convert(0, 'm', 'ft'), 0.0)
        self.assertAlmostEqual(converter.convert(0, 'km', 'in'), 0.0)

    def test_negative_distance(self):
        converter = DistanceConverter()
        with self.assertRaises(ValueError):
            converter.convert(-1, 'm', 'ft')

    def test_unsupported_conversion(self):
        converter = DistanceConverter()
        with self.assertRaises(ValueError):
            converter.convert(1, 'm', 'yd')

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'm', 'km'))
    print(converter.convert(1, 'km', 'ft'))
    unittest.main()