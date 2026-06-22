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
        key = f"{from_unit}_to_{to_unit}"
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError("Invalid conversion units")

if __name__ == '__main__':
    converter = LengthConverter()
    sample_values = [
        (1, 'm', 'km'),
        (2, 'm', 'cm'),
        (3, 'm', 'mm'),
        (4, 'm', 'in'),
        (5, 'm', 'ft'),
        (6, 'm', 'yd'),
        (7, 'm', 'mi')
    ]
    for value, from_unit, to_unit in sample_values:
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")