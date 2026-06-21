class VolumeConverter:
    LITER_TO_ML = 1000
    LITER_TO_GALLON = 0.264172
    LITER_TO_QUART = 1.05669
    LITER_TO_PINT = 2.11338
    LITER_TO_CUP = 4.22675
    LITER_TO_OZ = 33.814

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
        self._units = {'l': 'l', 'liter': 'l', 'liters': 'l',
                       'ml': 'ml', 'milliliter': 'ml', 'milliliters': 'ml',
                       'gal': 'gal', 'gallon': 'gal', 'gallons': 'gal',
                       'qt': 'qt', 'quart': 'qt', 'quarts': 'qt',
                       'pt': 'pt', 'pint': 'pt', 'pints': 'pt',
                       'c': 'c', 'cup': 'c', 'cups': 'c',
                       'oz': 'oz', 'fluidounce': 'oz', 'fluidounces': 'oz'}
        if self.unit not in self._units:
            raise ValueError(f"Unsupported unit: {self.unit}")
        self.unit = self._units[self.unit]

    def _to_liters(self, val, unit):
        if unit == 'l':
            return val
        if unit == 'ml':
            return val / self.LITER_TO_ML
        if unit == 'gal':
            return val / self.LITER_TO_GALLON
        if unit == 'qt':
            return val / self.LITER_TO_QUART
        if unit == 'pt':
            return val / self.LITER_TO_PINT
        if unit == 'c':
            return val / self.LITER_TO_CUP
        if unit == 'oz':
            return val / self.LITER_TO_OZ

    def _from_liters(self, val, unit):
        if unit == 'l':
            return val
        if unit == 'ml':
            return val * self.LITER_TO_ML
        if unit == 'gal':
            return val * self.LITER_TO_GALLON
        if unit == 'qt':
            return val * self.LITER_TO_QUART
        if unit == 'pt':
            return val * self.LITER_TO_PINT
        if unit == 'c':
            return val * self.LITER_TO_CUP
        if unit == 'oz':
            return val * self.LITER_TO_OZ

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in self._units:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        target_unit = self._units[target_unit]
        liters = self._to_liters(self.value, self.unit)
        result = self._from_liters(liters, target_unit)
        return result

if __name__ == '__main__':
    converter = VolumeConverter(10, 'gallons')
    print(converter.convert('liters'))
    print(converter.convert('ml'))
    print(converter.convert('fluidounces'))
    converter2 = VolumeConverter(500, 'ml')
    print(converter2.convert('cups'))