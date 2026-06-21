class VolumeConverter:
    LITERS = 1.0
    MILLILITERS = 0.001
    CUBIC_METERS = 1000.0
    GALLONS = 3.78541
    QUARTS = 0.946353
    PINTS = 0.473176
    FLUID_OUNCES = 0.0295735

    SUPPORTED_UNITS = {
        'liters': LITERS,
        'milliliters': MILLILITERS,
        'cubic_meters': CUBIC_METERS,
        'gallons': GALLONS,
        'quarts': QUARTS,
        'pints': PINTS,
        'fluid_ounces': FLUID_OUNCES
    }

    @staticmethod
    def to_base_unit(volume, unit):
        if unit not in VolumeConverter.SUPPORTED_UNITS:
            raise ValueError(f'Unsupported unit: {unit}')
        return volume * VolumeConverter.SUPPORTED_UNITS[unit]

    @staticmethod
    def from_base_unit(base_volume, target_unit):
        if target_unit not in VolumeConverter.SUPPORTED_UNITS:
            raise ValueError(f'Unsupported unit: {target_unit}')
        return base_volume / VolumeConverter.SUPPORTED_UNITS[target_unit]

if __name__ == '__main__':
    volume_in_liters = VolumeConverter.to_base_unit(5, 'gallons')
    print(f'5 gallons is {volume_in_liters} liters')

    volume_in_milliliters = VolumeConverter.from_base_unit(2, 'milliliters')
    print(f'2 liters is {volume_in_milliliters} milliliters')

    volume_in_cubic_meters = VolumeConverter.to_base_unit(1, 'cubic_meters')
    print(f'1 cubic meter is {volume_in_cubic_meters} liters')