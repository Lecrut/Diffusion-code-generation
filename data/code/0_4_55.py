class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Conversion factor must be a numeric value.")
        self.conversion_factors[target_unit] = factor

    def convert_to_base(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {unit} to {self.base_unit} is not supported.")
        return value * self.conversion_factors[unit]

    def convert_from_base(self, base_value, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {self.base_unit} to {target_unit} is not supported.")
        return base_value / self.conversion_factors[target_unit]

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit != self.base_unit:
            base_value = self.convert_to_base(value, from_unit)
        else:
            base_value = value

        if to_unit != self.base_unit:
            converted_value = self.convert_from_base(base_value, to_unit)
        else:
            converted_value = base_value

        return converted_value

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)
    converter.add_conversion_factor('inches', 0.0254)
    converter.add_conversion_factor('feet', 0.3048)
    converter.add_conversion_factor('yards', 0.9144)
    converter.add_conversion_factor('miles', 1609.34)

    value_in_meters = 10
    converted_to_cm = converter.convert(value_in_meters, 'meters', 'centimeters')
    converted_to_km = converter.convert(value_in_meters, 'meters', 'kilometers')
    converted_to_feet = converter.convert(value_in_meters, 'meters', 'feet')
    converted_to_yards = converter.convert(value_in_meters, 'meters', 'yards')
    converted_to_miles = converter.convert(value_in_meters, 'meters', 'miles')

    print(f'{value_in_meters} meters is equal to {converted_to_cm} centimeters')
    print(f'{value_in_meters} meters is equal to {converted_to_km} kilometers')
    print(f'{value_in_meters} meters is equal to {converted_to_feet} feet')
    print(f'{value_in_meters} meters is equal to {converted_to_yards} yards')
    print(f'{value_in_meters} meters is equal to {converted_to_miles} miles')