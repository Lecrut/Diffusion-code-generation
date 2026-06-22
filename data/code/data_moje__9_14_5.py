class VolumeConverter:
    LITERS_PER_GALLON = 3.785411784
    LITERS_PER_QUART = LITERS_PER_GALLON / 4
    LITERS_PER_PINT = LITERS_PER_QUART / 2
    LITERS_PER_CUP = LITERS_PER_PINT / 2
    LITERS_PER_FL_OZ = LITERS_PER_CUP / 8

    def __init__(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower == 'liter' or unit_lower == 'liters' or unit_lower == 'l':
            self.liters = value
        elif unit_lower == 'milliliter' or unit_lower == 'milliliters' or unit_lower == 'ml':
            self.liters = value / 1000
        elif unit_lower == 'gallon' or unit_lower == 'gallons' or unit_lower == 'gal':
            self.liters = value * VolumeConverter.LITERS_PER_GALLON
        elif unit_lower == 'quart' or unit_lower == 'quarts' or unit_lower == 'qt':
            self.liters = value * VolumeConverter.LITERS_PER_QUART
        elif unit_lower == 'pint' or unit_lower == 'pints' or unit_lower == 'pt':
            self.liters = value * VolumeConverter.LITERS_PER_PINT
        elif unit_lower == 'cup' or unit_lower == 'cups' or unit_lower == 'c':
            self.liters = value * VolumeConverter.LITERS_PER_CUP
        elif unit_lower == 'fluid ounce' or unit_lower == 'fluid ounces' or unit_lower == 'fl oz' or unit_lower == 'floz':
            self.liters = value * VolumeConverter.LITERS_PER_FL_OZ
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def to_liters(self):
        return self.liters

    def to_milliliters(self):
        return self.liters * 1000

    def to_gallons(self):
        return self.liters / VolumeConverter.LITERS_PER_GALLON

    def to_quarts(self):
        return self.liters / VolumeConverter.LITERS_PER_QUART

    def to_pints(self):
        return self.liters / VolumeConverter.LITERS_PER_PINT

    def to_cups(self):
        return self.liters / VolumeConverter.LITERS_PER_CUP

    def to_fluid_ounces(self):
        return self.liters / VolumeConverter.LITERS_PER_FL_OZ

    def convert(self, target_unit):
        target_lower = target_unit.lower()
        if target_lower == 'liter' or target_lower == 'liters' or target_lower == 'l':
            return self.liters
        elif target_lower == 'milliliter' or target_lower == 'milliliters' or target_lower == 'ml':
            return self.liters * 1000
        elif target_lower == 'gallon' or target_lower == 'gallons' or target_lower == 'gal':
            return self.liters / VolumeConverter.LITERS_PER_GALLON
        elif target_lower == 'quart' or target_lower == 'quarts' or target_lower == 'qt':
            return self.liters / VolumeConverter.LITERS_PER_QUART
        elif target_lower == 'pint' or target_lower == 'pints' or target_lower == 'pt':
            return self.liters / VolumeConverter.LITERS_PER_PINT
        elif target_lower == 'cup' or target_lower == 'cups' or target_lower == 'c':
            return self.liters / VolumeConverter.LITERS_PER_CUP
        elif target_lower == 'fluid ounce' or target_lower == 'fluid ounces' or target_lower == 'fl oz' or target_lower == 'floz':
            return self.liters / VolumeConverter.LITERS_PER_FL_OZ
        else:
            raise ValueError(f"Unsupported unit: {target_unit}")

if __name__ == '__main__':
    converter = VolumeConverter(1, 'gallon')
    print(converter.convert('liters'))
    print(converter.convert('quarts'))
    print(converter.convert('pints'))
    print(converter.convert('cups'))
    print(converter.convert('fluid ounces'))
    print(converter.convert('milliliters'))
    converter2 = VolumeConverter(500, 'milliliters')
    print(converter2.convert('liters'))
    print(converter2.convert('gallons'))
    print(converter2.convert('cups'))