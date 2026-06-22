class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        self.conversion_factors[target_unit] = factor

    def convert(self, value, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Conversion to {target_unit} is not supported.")
        return value * self.conversion_factors[target_unit]

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)

    value_in_meters = 5
    converted_to_cm = converter.convert(value_in_meters, 'centimeters')
    converted_to_km = converter.convert(value_in_meters, 'kilometers')

    print(f"{value_in_meters} meters is {converted_to_cm} centimeters")
    print(f"{value_in_meters} meters is {converted_to_km} kilometers")