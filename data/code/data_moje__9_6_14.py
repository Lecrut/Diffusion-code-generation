VOLUME_CONSTANTS = {
    'ml': 0.001,
    'l': 1.0,
    'gal': 3.78541,
    'm3': 1000.0,
    'qt': 0.946353,
    'pt': 0.473176,
    'cup': 0.236588,
    'floz': 0.0295735,
    'tbsp': 0.0147868,
    'tsp': 0.00492892
}

class VolumeConverter:
    def __init__(self, constants_dict):
        self.constants = constants_dict

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.constants:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.constants:
            raise ValueError(f"Unknown target unit: {to_unit}")
        
        base_value = value * self.constants[from_unit]
        result = base_value / self.constants[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter(VOLUME_CONSTANTS)
    
    sample_results = []
    
    result1 = converter.convert(1, 'l', 'ml')
    sample_results.append(result1)
    
    result2 = converter.convert(1, 'm3', 'gal')
    sample_results.append(result2)
    
    result3 = converter.convert(5, 'gal', 'l')
    sample_results.append(result3)
    
    result4 = converter.convert(100, 'ml', 'floz')
    sample_results.append(result4)
    
    for res in sample_results:
        print(res)