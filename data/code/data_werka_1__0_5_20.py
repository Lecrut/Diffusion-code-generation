class UnitConverter:
    def __init__(self):
        self.base_unit = 'meters'
        self.conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.344,
            'nautical_miles': 1852.0
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversion_factors[from_unit]
        converted_value = base_value / self.conversion_factors[to_unit]
        return converted_value

def main():
    converter = UnitConverter()
    
    result1 = converter.convert(1, 'kilometers', 'meters')
    print(f"1 kilometer = {result1} meters")
    
    result2 = converter.convert(5280, 'feet', 'miles')
    print(f"5280 feet = {result2} miles")
    
    result3 = converter.convert(100, 'centimeters', 'inches')
    print(f"100 centimeters = {result3:.4f} inches")

if __name__ == '__main__':
    main()