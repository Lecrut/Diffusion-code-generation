class VolumeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self._conversion_factors = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.785411784,
            'quart': 0.946352946,
            'pint': 0.473176473,
            'cup': 0.2365882365,
            'fluid_ounce': 0.0295735295625
        }

    def _to_liters(self):
        factor = self._conversion_factors[self.unit]
        return self.value * factor

    def _from_liters(self, liters, target_unit):
        factor = self._conversion_factors[target_unit]
        return liters / factor

    def convert(self, target_unit):
        liters = self._to_liters()
        return self._from_liters(liters, target_unit)

    def convert_all(self):
        units = ['liter', 'milliliter', 'gallon', 'quart', 'pint', 'cup', 'fluid_ounce']
        results = {}
        liters = self._to_liters()
        for unit in units:
            results[unit] = self._from_liters(liters, unit)
        return results

if __name__ == '__main__':
    converter = VolumeConverter(1.0, 'gallon')
    print(f"1 gallon in liters: {converter.convert('liter')}")
    print(f"1 gallon in milliliters: {converter.convert('milliliter')}")
    print(f"1 gallon in quarts: {converter.convert('quart')}")
    print(f"1 gallon in pints: {converter.convert('pint')}")
    print(f"1 gallon in cups: {converter.convert('cup')}")
    print(f"1 gallon in fluid ounces: {converter.convert('fluid_ounce')}")
    all_conversions = converter.convert_all()
    print(f"All conversions: {all_conversions}")