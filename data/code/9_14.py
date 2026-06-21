class VolumeConverter:
    LITER_TO_BASE = 1.0
    MILLILITER_TO_BASE = 0.001
    GALLON_TO_BASE = 3.785411784
    QUART_TO_BASE = 0.946352946
    PINT_TO_BASE = 0.473176473
    CUP_TO_BASE = 0.236588236
    FLUID_OUNCE_TO_BASE = 0.0295735296

    CONVERSION_TABLE = {
        'liter': LITER_TO_BASE,
        'milliliter': MILLILITER_TO_BASE,
        'gallon': GALLON_TO_BASE,
        'quart': QUART_TO_BASE,
        'pint': PINT_TO_BASE,
        'cup': CUP_TO_BASE,
        'fluid_ounce': FLUID_OUNCE_TO_BASE
    }

    VALID_UNITS = set(CONVERSION_TABLE.keys())

    def __init__(self, value, unit):
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid unit: {unit}. Must be one of {self.VALID_UNITS}")
        self.base_value = value * self.CONVERSION_TABLE[unit]

    def convert(self, target_unit):
        if target_unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid target unit: {target_unit}. Must be one of {self.VALID_UNITS}")
        return self.base_value / self.CONVERSION_TABLE[target_unit]

    def get_base_value(self):
        return self.base_value

    def to_milliliters(self):
        return self.convert('milliliter')

    def to_liters(self):
        return self.convert('liter')

    def to_gallons(self):
        return self.convert('gallon')

    def to_quarts(self):
        return self.convert('quart')

    def to_pints(self):
        return self.convert('pint')

    def to_cups(self):
        return self.convert('cup')

    def to_fluid_ounces(self):
        return self.convert('fluid_ounce')

    def __repr__(self):
        return f"VolumeConverter(base={self.base_value:.4f} liters)"

if __name__ == '__main__':
    converter = VolumeConverter(2.5, 'gallon')
    print(f"Original: 2.5 gallons")
    print(f"Liters: {converter.to_liters()}")
    print(f"Milliliters: {converter.to_milliliters()}")
    print(f"Quarts: {converter.to_quarts()}")
    print(f"Pints: {converter.to_pints()}")
    print(f"Cups: {converter.to_cups()}")
    print(f"Fluid Ounces: {converter.to_fluid_ounces()}")
    print(f"Custom Conversion to liters: {converter.convert('liter')}")
    print(f"Repr output: {repr(converter)}")