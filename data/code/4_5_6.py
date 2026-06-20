class DistanceConverter:
    def __init__(self):
        self.base_unit = 'meters'
        self.conversion_to_base = {
            'meters': 1.0,
            'metres': 1.0,
            'm': 1.0,
            'kilometers': 1000.0,
            'kilometres': 1000.0,
            'km': 1000.0,
            'centimeters': 0.01,
            'centimetres': 0.01,
            'cm': 0.01,
            'millimeters': 0.001,
            'millimetres': 0.001,
            'mm': 0.001,
            'miles': 1609.344,
            'mile': 1609.344,
            'mi': 1609.344,
            'yards': 0.9144,
            'yard': 0.9144,
            'yd': 0.9144,
            'feet': 0.3048,
            'foot': 0.3048,
            'ft': 0.3048,
            'inches': 0.0254,
            'inch': 0.0254,
            'in': 0.0254,
            'nautical_miles': 1852.0,
            'nautical_mile': 1852.0,
            'nm': 1852.0
        }

    def normalize_unit(self, unit_string):
        cleaned = unit_string.strip().lower()
        if cleaned in self.conversion_to_base:
            return cleaned
        return None

    def convert(self, value, from_unit, to_unit):
        from_norm = self.normalize_unit(from_unit)
        to_norm = self.normalize_unit(to_unit)

        if from_norm is None:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_norm is None:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        base_value = value * self.conversion_to_base[from_norm]
        result = base_value / self.conversion_to_base[to_norm]
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_cases = [
        (1000, 'meters', 'kilometers'),
        (1, 'mile', 'kilometers'),
        (5.5, 'feet', 'meters'),
        (100, 'centimeters', 'inches'),
        (0.5, 'nautical_miles', 'meters')
    ]
    
    for value, frm, to in sample_cases:
        converted = converter.convert(value, frm, to)
        print(f"{value} {frm} = {converted} {to}")
        
    try:
        converter.convert(10, 'lightyears', 'meters')
    except ValueError as e:
        print(e)