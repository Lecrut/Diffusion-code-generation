class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm_to_km': 0.001,
            'm_to_cm': 100,
            'm_to_mm': 1000,
            'm_to_in': 39.3701,
            'm_to_ft': 3.28084,
            'm_to_yd': 1.09361,
            'm_to_mi': 0.000621371,
            'km_to_m': 1000,
            'cm_to_m': 0.01,
            'mm_to_m': 0.001,
            'in_to_m': 0.0254,
            'ft_to_m': 0.3048,
            'yd_to_m': 0.9144,
            'mi_to_m': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        factor_key = f"{from_unit}_to_{to_unit}"
        if factor_key in self.conversion_factors:
            return value * self.conversion_factors[factor_key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    sample_values = [
        (10, 'm', 'km'),
        (500, 'cm', 'm'),
        (2000, 'mm', 'm'),
        (72, 'in', 'm'),
        (6, 'ft', 'm'),
        (3, 'yd', 'm'),
        (1, 'mi', 'm')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.4f} {to_unit}")