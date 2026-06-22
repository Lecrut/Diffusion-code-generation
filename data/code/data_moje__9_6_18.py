class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'ml': 1.0,
            'l': 1000.0,
            'gal': 3785.411784,
            'm3': 1000000.0,
            'ft3': 28316.846592,
            'cup': 236.5882365
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")
            
        value_in_ml = value * self.conversion_factors[from_unit]
        result = value_in_ml / self.conversion_factors[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    
    result_1 = converter.convert(1, 'l', 'ml')
    print(result_1)
    
    result_2 = converter.convert(1, 'm3', 'gal')
    print(result_2)
    
    result_3 = converter.convert(2, 'gal', 'l')
    print(result_3)
    
    result_4 = converter.convert(5, 'ft3', 'm3')
    print(result_4)
    
    result_5 = converter.convert(1, 'cup', 'ml')
    print(result_5)