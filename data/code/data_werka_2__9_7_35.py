class VolumeConverter:
    def __init__(self):
        self.conversion_table = {
            'liters': {'base_value': 1.0},
            'milliliters': {'base_value': 0.001},
            'cubic_meters': {'base_value': 1000.0},
            'gallons': {'base_value': 3.78541},
            'quarts': {'base_value': 0.946353},
            'pints': {'base_value': 0.473176},
            'fluid_ounces': {'base_value': 0.0295735}
        }

    def to_base_unit(self, volume, unit):
        if unit not in self.conversion_table:
            raise ValueError(f'Unsupported unit: {unit}')
        return volume * self.conversion_table[unit]['base_value']

    def from_base_unit(self, base_volume, target_unit):
        if target_unit not in self.conversion_table:
            raise ValueError(f'Unsupported unit: {target_unit}')
        return base_volume / self.conversion_table[target_unit]['base_value']

if __name__ == '__main__':
    converter = VolumeConverter()
    volume_in_liters = converter.to_base_unit(5, 'gallons')
    print(f'5 gallons is {volume_in_liters} liters')

    volume_in_milliliters = converter.from_base_unit(1.5, 'milliliters')
    print(f'1.5 liters is {volume_in_milliliters} milliliters')

    volume_in_cubic_meters = converter.to_base_unit(2, 'cubic_meters')
    print(f'2 cubic meters is {volume_in_cubic_meters} liters')

    volume_in_gallons = converter.from_base_unit(1000, 'gallons')
    print(f'1000 milliliters is {volume_in_gallons} gallons')