class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'liters_to_milliliters': 1000,
            'milliliters_to_liters': 0.001,
            'liters_to_gallons': 0.264172,
            'gallons_to_liters': 3.78541,
            'liters_to_quarts': 1.05669,
            'quarts_to_liters': 0.946353,
            'liters_to_pints': 2.11338,
            'pints_to_liters': 0.473176,
            'liters_to_cups': 4.22675,
            'cups_to_liters': 0.236588,
            'liters_to_fluid_ounces': 33.814,
            'fluid_ounces_to_liters': 0.0295735
        }

    def convert(self, value, from_unit, to_unit):
        key = f"{from_unit.lower()}_to_{to_unit.lower()}"
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError("Invalid conversion units")

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 1.0
    print(f"{sample_value} liters to milliliters: {converter.convert(sample_value, 'liters', 'milliliters')}")
    print(f"{sample_value} gallons to liters: {converter.convert(sample_value, 'gallons', 'liters')}")
    print(f"{sample_value} quarts to pints: {converter.convert(sample_value, 'quarts', 'pints')}")
    print(f"{sample_value} cups to fluid ounces: {converter.convert(sample_value, 'cups', 'fluid_ounces')}")