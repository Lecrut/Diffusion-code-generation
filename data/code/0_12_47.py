class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Unsupported unit")
        
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        
        return (value * factor_from) / factor_to

if __name__ == '__main__':
    converter = LengthConverter()
    
    sample_values = [
        (10, 'm', 'km'),
        (5, 'cm', 'in'),
        (2, 'yd', 'm'),
        (1, 'mi', 'ft')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.4f} {to_unit}")