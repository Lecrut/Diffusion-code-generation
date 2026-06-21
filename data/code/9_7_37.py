class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters': 1.0, 'milliliters': 0.001, 'cubic_meters': 1000.0, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'fluid_ounces': 0.0295735}

    def convert_to_liters(self, volume, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {unit}')
        return volume * self.conversion_factors[unit]

    def convert_from_liters(self, liters, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {target_unit}')
        return liters / self.conversion_factors[target_unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    volume_in_liters = converter.convert_to_liters(5, 'gallons')
    print(f'5 gallons is {volume_in_liters} liters')
    volume_in_milliliters = converter.convert_from_liters(2, 'milliliters')
    print(f'2 liters is {volume_in_milliliters} milliliters')
    volume_in_cubic_meters = converter.convert_to_liters(1, 'cubic_meters')
    print(f'1 cubic meter is {volume_in_cubic_meters} liters')
    volume_in_quarts = converter.convert_from_liters(9.46353, 'quarts')
    print(f'9.46353 liters is {volume_in_quarts} quarts')