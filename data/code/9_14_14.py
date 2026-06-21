class VolumeConverter:
    _to_liters = {
        'liter': 1.0,
        'liters': 1.0,
        'ml': 0.001,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'gallon': 3.785411784,
        'gallons': 3.785411784,
        'quart': 0.946352946,
        'quarts': 0.946352946,
        'pint': 0.473176473,
        'pints': 0.473176473,
        'cup': 0.2365882365,
        'cups': 0.2365882365,
        'fluid ounce': 0.0295735296875,
        'fl_ounce': 0.0295735296875,
        'fl oz': 0.0295735296875,
        'fluidounce': 0.0295735296875,
        'ounce': 0.0295735296875,
    }

    def __init__(self, value, from_unit):
        self.value = value
        self.from_unit = from_unit.lower().replace(' ', '').replace('_', '').replace('-', '')
        self.liters = value * self._to_liters.get(self.from_unit, 0.0)

    def convert(self, to_unit):
        to_key = to_unit.lower().replace(' ', '').replace('_', '').replace('-', '')
        factor = self._to_liters.get(to_key, 0.0)
        if factor == 0.0:
            raise ValueError(f"Unsupported unit: {to_unit}")
        return self.liters / factor

    def to_ml(self):
        return self.convert('ml')

    def to_liters(self):
        return self.liters

    def to_gallons(self):
        return self.convert('gallon')

    def to_quarts(self):
        return self.convert('quart')

    def to_pints(self):
        return self.convert('pint')

    def to_cups(self):
        return self.convert('cup')

    def to_fluid_ounces(self):
        return self.convert('fluid ounce')

if __name__ == '__main__':
    converter = VolumeConverter(1.0, 'gallon')
    print(converter.to_liters())
    print(converter.to_ml())
    print(converter.to_quarts())
    print(converter.to_pints())
    print(converter.to_cups())
    print(converter.to_fluid_ounces())

    converter2 = VolumeConverter(500, 'ml')
    print(converter2.to_liters())
    print(converter2.to_gallons())