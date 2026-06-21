class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Conversion factor must be a numeric value.")
        self.conversion_factors[target_unit] = factor

    def convert_to_base(self, value, unit):
        if unit == self.base_unit:
            return value
        if unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {unit} to {self.base_unit} is not supported.")
        return value * self.conversion_factors[unit]

    def convert_from_base(self, base_value, target_unit):
        if target_unit == self.base_unit:
            return base_value
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {self.base_unit} to {target_unit} is not supported.")
        return base_value / self.conversion_factors[target_unit]

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        base_value = self.convert_to_base(value, from_unit)
        converted_value = self.convert_from_base(base_value, to_unit)
        return converted_value

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)

    value_in_meters = 5
    converted_to_cm = converter.convert(value_in_meters, 'meters', 'centimeters')
    converted_to_km = converter.convert(value_in_meters, 'meters', 'kilometers')
    print(f"{value_in_meters} meters is {converted_to_cm} centimeters")
    print(f"{value_in_meters} meters is {converted_to_km} kilometers")

    value_in_cm = 100
    converted_back_to_m = converter.convert(value_in_cm, 'centimeters', 'meters')
    print(f"{value_in_cm} centimeters is {converted_back_to_m} meters")