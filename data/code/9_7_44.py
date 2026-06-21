class VolumeConverter:
    LITERS = 1.0
    MILLILITERS = 0.001
    CUBIC_METERS = 1000.0
    GALLONS = 3.78541
    QUARTS = 0.946353
    PINTS = 0.473176
    FLUID_OUNCES = 0.0295735
    SUPPORTED_UNITS = {'liters': LITERS, 'milliliters': MILLILITERS, 'cubic_meters': CUBIC_METERS, 'gallons': GALLONS, 'quarts': QUARTS, 'pints': PINTS, 'fluid_ounces': FLUID_OUNCES}

    def __init__(self):
        self.conversion_factors = self.SUPPORTED_UNITS

    def to_base_unit(self, volume, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {unit}')
        return volume * self.conversion_factors[unit]

    def from_base_unit(self, base_volume, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {target_unit}')
        return base_volume / self.conversion_factors[target_unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    volume_in_liters = converter.to_base_unit(10, 'quarts')
    print(f'10 quarts is {volume_in_liters} liters')
    volume_in_milliliters = converter.from_base_unit(5, 'milliliters')
    print(f'5 liters is {volume_in_milliliters} milliliters')
    volume_in_gallons = converter.to_base_unit(2, 'cubic_meters') / self.GALLONS
    print(f'2 cubic meters is {volume_in_gallons} gallons')