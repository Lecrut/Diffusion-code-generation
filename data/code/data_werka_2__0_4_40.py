class ConversionManager:
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
        return self.convert_from_base(base_value, to_unit)

if __name__ == '__main__':
    manager = ConversionManager('meters')
    manager.add_conversion_factor('centimeters', 0.01)
    manager.add_conversion_factor('millimeters', 0.001)
    manager.add_conversion_factor('kilometers', 1000)

    sample_value = 5
    converted_to_cm = manager.convert(sample_value, 'meters', 'centimeters')
    converted_to_mm = manager.convert(sample_value, 'meters', 'millimeters')
    converted_to_km = manager.convert(sample_value, 'meters', 'kilometers')

    print(f"{sample_value} meters is {converted_to_cm} centimeters")
    print(f"{sample_value} meters is {converted_to_mm} millimeters")
    print(f"{sample_value} meters is {converted_to_km} kilometers")