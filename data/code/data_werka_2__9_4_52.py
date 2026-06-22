class VolumeConverter:
    def __init__(self):
        self.base_units = {
            'L': 1,
            'ml': 0.001,
            'm3': 1,
            'gal': 0.264172
        }
    
    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.base_units or to_unit not in self.base_units:
            raise ValueError(f'Conversion between {from_unit} and {to_unit} is not supported')
        
        base_value = value * self.base_units[from_unit]
        converted_value = base_value / self.base_units[to_unit]
        return converted_value

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))