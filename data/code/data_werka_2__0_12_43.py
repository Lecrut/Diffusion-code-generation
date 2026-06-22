class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm_to_km': 1e-3,
            'm_to_cm': 1e2,
            'm_to_mm': 1e3,
            'm_to_in': 39.3701,
            'm_to_ft': 3.28084,
            'm_to_yd': 1.09361,
            'm_to_mi': 6.21371e-4,
            'km_to_m': 1e3,
            'cm_to_m': 1e-2,
            'mm_to_m': 1e-3,
            'in_to_m': 0.0254,
            'ft_to_m': 0.3048,
            'yd_to_m': 0.9144,
            'mi_to_m': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')

if __name__ == '__main__':
    converter = LengthConverter()
    sample_values = [
        (10, 'm', 'km'),
        (25.4, 'cm', 'in'),
        (1000, 'mm', 'm'),
        (39.3701, 'in', 'm'),
        (3.28084, 'ft', 'm'),
        (1.09361, 'yd', 'm'),
        (6.21371e-4, 'mi', 'm')
    ]
    for value, from_unit, to_unit in sample_values:
        result = converter.convert(value, from_unit, to_unit)
        print(f'{value} {from_unit} is {result} {to_unit}')