class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters': 1.0, 'milliliters': 0.001, 'cubic_meters': 1000.0, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'fluid_ounces': 0.0295735}

    def to_base_unit(self, value, unit):
        return value * self.conversion_factors[unit]

    def from_base_unit(self, value_in_liters, target_unit):
        return value_in_liters / self.conversion_factors[target_unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.to_base_unit(5, 'gallons')
    print(f'5 gallons is {gallons_to_liters} liters')
    milliliters_to_quarts = converter.from_base_unit(2000, 'quarts')
    print(f'2000 milliliters is {milliliters_to_quarts} quarts')