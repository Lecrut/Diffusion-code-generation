class UnitConverter:
    def __init__(self):
        self.base_unit = 'meters'
        self.conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.344,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversion_factors[from_unit]
        result = base_value / self.conversion_factors[to_unit]
        return result

    def add_unit(self, unit_name, factor):
        self.conversion_factors[unit_name] = factor

if __name__ == '__main__':
    converter = UnitConverter()
    
    result1 = converter.convert(1000, 'meters', 'kilometers')
    print(result1)
    
    result2 = converter.convert(1, 'miles', 'meters')
    print(result2)
    
    result3 = converter.convert(5, 'feet', 'centimeters')
    print(result3)
    
    result4 = converter.convert(100, 'centimeters', 'inches')
    print(result4)
    
    converter.add_unit('light_years', 9.461e15)
    result5 = converter.convert(1, 'light_years', 'kilometers')
    print(result5)