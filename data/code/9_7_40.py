class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters': 1.0, 'milliliters': 0.001, 'cubic_meters': 1000.0, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'fluid_ounces': 0.0295735}

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
    volume_in_liters = converter.to_base_unit(10, 'gallons')
    print(f'10 gallons is {volume_in_liters} liters')
    volume_in_milliliters = converter.from_base_unit(0.5, 'milliliters')
    print(f'0.5 liters is {volume_in_milliliters} milliliters')
    volume_in_cubic_meters = converter.to_base_unit(2, 'cubic_meters')
    print(f'2 cubic meters is {volume_in_cubic_meters} liters')
    volume_in_pints = converter.from_base_unit(1.4195, 'pints')
    print(f'1.4195 liters is {volume_in_pints} pints')