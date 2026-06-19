class UnitConverter:
    def __init__(self):
        self.conversions = {
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
        if from_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversions:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_value = value * self.conversions[from_unit]
        result = base_value / self.conversions[to_unit]
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    
    val1 = converter.convert(1, 'kilometers', 'meters')
    print(val1)
    
    val2 = converter.convert(5280, 'feet', 'miles')
    print(val2)
    
    val3 = converter.convert(100, 'centimeters', 'inches')
    print(val3)