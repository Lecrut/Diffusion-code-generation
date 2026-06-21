class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000.0
    LITERS_TO_CUBIC_METERS = 0.001
    GALLONS_TO_LITERS = 3.78541
    QUARTS_TO_LITERS = 0.946353
    PINTS_TO_LITERS = 0.473176
    FLUID_OUNCES_TO_LITERS = 0.0295735

    SUPPORTED_UNITS = {
        'liters': 1.0,
        'milliliters': LITERS_TO_MILLILITERS,
        'cubic_meters': LITERS_TO_CUBIC_METERS,
        'gallons': GALLONS_TO_LITERS,
        'quarts': QUARTS_TO_LITERS,
        'pints': PINTS_TO_LITERS,
        'fluid_ounces': FLUID_OUNCES_TO_LITERS
    }

    def to_base_unit(self, volume, unit):
        if unit not in self.SUPPORTED_UNITS:
            raise ValueError(f'Unsupported unit: {unit}')
        return volume * self.SUPPORTED_UNITS[unit]

    def from_base_unit(self, base_volume, target_unit):
        if target_unit not in self.SUPPORTED_UNITS:
            raise ValueError(f'Unsupported unit: {target_unit}')
        return base_volume / self.SUPPORTED_UNITS[target_unit]

if __name__ == '__main__':
    converter = VolumeConverter()
    volume_in_liters = converter.to_base_unit(5, 'gallons')
    print(f'5 gallons is {volume_in_liters} liters')
    
    volume_in_milliliters = converter.from_base_unit(2, 'milliliters')
    print(f'2 liters is {volume_in_milliliters} milliliters')
    
    volume_in_cubic_meters = converter.to_base_unit(1, 'cubic_meters')
    print(f'1 cubic meter is {volume_in_cubic_meters} liters')