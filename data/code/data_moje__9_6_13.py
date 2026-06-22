def create_converter():
    units = {
        'L': 1.0,
        'ml': 0.001,
        'm3': 1000.0,
        'gal': 3.78541,
        'pt': 0.473176,
        'qt': 0.946353
    }
    
    class VolumeConverter:
        def __init__(self):
            self.factors = units
            
        def convert(self, value, from_unit, to_unit):
            if from_unit not in self.factors or to_unit not in self.factors:
                raise ValueError(f"Unknown unit: {from_unit} or {to_unit}")
            base_volume = value * self.factors[from_unit]
            return base_volume / self.factors[to_unit]
            
    return VolumeConverter()

if __name__ == '__main__':
    converter = create_converter()
    result = converter.convert(5, 'L', 'ml')
    print(result)