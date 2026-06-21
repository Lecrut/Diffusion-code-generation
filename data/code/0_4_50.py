class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        self.conversion_factors[target_unit] = factor

    def convert_to_base(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {unit} to {self.base_unit} is not supported.")
        return value * self.conversion_factors[unit]

    def convert_from_base(self, base_value, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Conversion from {self.base_unit} to {target_unit} is not supported.")
        return base_value / self.conversion_factors[target_unit]

    def convert_between_units(self, value, from_unit, to_unit):
        if from_unit == self.base_unit:
            return self.convert_from_base(value, to_unit)
        elif to_unit == self.base_unit:
            return self.convert_to_base(value, from_unit)
        else:
            base_value = self.convert_to_base(value, from_unit)
            return self.convert_from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)
    
    value_cm = 250
    value_km = 5
    
    converted_to_meters_from_cm = converter.convert_between_units(value_cm, 'centimeters', 'meters')
    converted_to_meters_from_km = converter.convert_between_units(value_km, 'kilometers', 'meters')
    
    print(f"{value_cm} centimeters is {converted_to_meters_from_cm} meters")
    print(f"{value_km} kilometers is {converted_to_meters_from_km} meters")