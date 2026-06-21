class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'pints_to_quarts': 0.5,
            'quarts_to_pints': 2.0
        }

    def convert(self, volume, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit conversion from {from_unit} to {to_unit}")
        
        if from_unit == to_unit:
            return volume
        
        key = f"{from_unit}_to_{to_unit}"
        if key not in self.conversion_factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not directly supported")
        
        return volume * self.conversion_factors[key]

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_pints = 16
    quarts = converter.convert(sample_pints, 'pints', 'quarts')
    print(quarts)