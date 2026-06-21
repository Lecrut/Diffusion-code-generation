class VolumeConverter:
    BASE_UNIT = 'liters'
    SUPPORTED_UNITS = {BASE_UNIT: 1.0, 'milliliters': 0.001, 'cubic_meters': 1000.0, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'fluid_ounces': 0.0295735}

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
    volume_in_cubic_meters = converter.from_base_unit(2, 'cubic_meters')
    print(f'2 liters is {volume_in_cubic_meters} cubic meters')
    volume_in_liters_from_pints = converter.to_base_unit(10, 'pints')
    print(f'10 pints is {volume_in_liters_from_pints} liters')
    volume_in_milliliters = converter.from_base_unit(1, 'quarts') * self.SUPPORTED_UNITS['milliliters']
    print(f'1 quart is {volume_in_milliliters} milliliters')