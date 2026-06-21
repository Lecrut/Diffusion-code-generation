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
        base_value = self.convert_to_base(value, from_unit)
        converted_value = self.convert_from_base(base_value, to_unit)
        return converted_value

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 0.01)
    converter.add_conversion_factor('kilometers', 1000)

    sample_value_meters = 15
    sample_from_unit = 'meters'
    sample_to_unit = 'kilometers'

    converted_value_km = converter.convert(sample_value_meters, sample_from_unit, sample_to_unit)
    print(f"{sample_value_meters} {sample_from_unit} is equal to {converted_value_km} {sample_to_unit}")