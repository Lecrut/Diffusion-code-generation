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
    volume_in_liters = converter.to_base_unit(10, 'quarts')
    print(f'10 quarts is {volume_in_liters} liters')
    volume_in_cubic_meters = converter.from_base_unit(0.5, 'cubic_meters')
    print(f'0.5 liters is {volume_in_cubic_meters} cubic meters')
    volume_in_liters_gallons = converter.to_base_unit(3, 'gallons')
    print(f'3 gallons is {volume_in_liters_gallons} liters')
    volume_in_fluid_ounces = converter.from_base_unit(0.118294, 'fluid_ounces')
    print(f'0.118294 liters is {volume_in_fluid_ounces} fluid ounces')