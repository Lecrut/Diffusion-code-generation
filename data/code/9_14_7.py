class VolumeConverter:
    _to_liters = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons': 3.785411784,
        'quarts': 0.946352946,
        'pints': 0.473176473,
        'cups': 0.2365882365,
        'fluid_ounces': 0.0295735295625
    }

    def __init__(self, value, unit):
        self._value = value
        self._unit = unit.lower().replace(' ', '_')
        if self._unit not in self._to_liters:
            raise ValueError(f"Unsupported unit: {self._unit}")

    def _to_liters(self):
        factor = self._to_liters[self._unit]
        return self._value * factor

    def convert_to(self, target_unit):
        target_unit = target_unit.lower().replace(' ', '_')
        if target_unit not in self._to_liters:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        liters = self._to_liters[self._unit] * self._value
        target_factor = self._to_liters[target_unit]
        return liters / target_factor

if __name__ == '__main__':
    converter = VolumeConverter(1, 'gallons')
    result_mliters = converter.convert_to('milliliters')
    result_liters = converter.convert_to('liters')
    result_cups = converter.convert_to('cups')
    print(f"1 gallon in milliliters: {result_mliters}")
    print(f"1 gallon in liters: {result_liters}")
    print(f"1 gallon in cups: {result_cups}")

    converter2 = VolumeConverter(500, 'milliliters')
    result_fluid_ounces = converter2.convert_to('fluid_ounces')
    result_gallons = converter2.convert_to('gallons')
    print(f"500 milliliters in fluid ounces: {result_fluid_ounces}")
    print(f"500 milliliters in gallons: {result_gallons}")