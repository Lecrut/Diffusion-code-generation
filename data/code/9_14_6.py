class VolumeConverter:
    def __init__(self):
        self.units = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.785411784,
            'quart': 0.946352946,
            'pint': 0.473176473,
            'cup': 0.2365882365,
            'fluid_ounce': 0.0295735295625
        }

    def convert(self, amount, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Unsupported unit")
        
        base_value = amount * self.units[from_unit]
        result = base_value / self.units[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'liter', 'milliliter'))
    print(converter.convert(1, 'gallon', 'liter'))
    print(converter.convert(16, 'fluid_ounce', 'cup'))