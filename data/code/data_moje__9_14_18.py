class VolumeConverter:
    LITERS_TO_BASE = 1.0
    MILLILITERS_TO_BASE = 0.001
    GALLONS_TO_BASE = 3.785411784
    QUARTS_TO_BASE = 0.946352946
    PINTS_TO_BASE = 0.473176473
    CUPS_TO_BASE = 0.236588237
    FLUID_OUNCES_TO_BASE = 0.0295735296

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self._base_value = value * self._get_conversion_factor(unit)

    def _get_conversion_factor(self, unit):
        factors = {
            'liter': self.LITERS_TO_BASE,
            'milliliter': self.MILLILITERS_TO_BASE,
            'gallon': self.GALLONS_TO_BASE,
            'quart': self.QUARTS_TO_BASE,
            'pint': self.PINTS_TO_BASE,
            'cup': self.CUPS_TO_BASE,
            'fluid_ounce': self.FLUID_OUNCES_TO_BASE
        }
        return factors.get(unit, 0.0)

    def convert(self, target_unit):
        factor = self._get_conversion_factor(target_unit)
        if factor == 0.0:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return self._base_value / factor

    def to_liters(self):
        return self.convert('liter')

    def to_milliliters(self):
        return self.convert('milliliter')

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

if __name__ == '__main__':
    converter = VolumeConverter(1.0, 'liter')
    print(converter.to_milliliters())
    print(converter.to_gallons())
    print(converter.to_cups())
    print(converter.convert('fluid_ounce'))