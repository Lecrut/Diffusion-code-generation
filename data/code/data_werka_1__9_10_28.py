class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters': 1.0, 'milliliters': 0.001, 'cubic_meters': 1000.0, 'cubic_centimeters': 0.001, 'gallons': 3.78541, 'quarts': 0.946353, 'pints': 0.473176, 'fluid_ounces': 0.0295735}

    def to_base_unit(self, value, unit):
        return value * self.conversion_factors[unit]

    def from_base_unit(self, base_value, target_unit):
        return base_value / self.conversion_factors[target_unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    base_liters = converter.to_base_unit(5, 'gallons')
    print(f'5 gallons is {base_liters} liters')
    converted_ml = converter.from_base_unit(2000, 'milliliters')
    print(f'2000 milliliters is {converted_ml} liters')