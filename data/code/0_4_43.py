class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Conversion factor must be a numeric value.")
        self.conversion_factors[target_unit] = factor

    def _validate_units(self, from_unit, to_unit):
        if from_unit != self.base_unit:
            raise ValueError(f"Conversions must start from the base unit: {self.base_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Conversion to {to_unit} is not supported.")

    def convert(self, value, from_unit, to_unit):
        self._validate_units(from_unit, to_unit)
        return value * self.conversion_factors[to_unit]

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)
    
    sample_value = 5.0
    from_unit = 'meters'
    to_unit_cm = 'centimeters'
    to_unit_km = 'kilometers'
    
    converted_to_cm = converter.convert(sample_value, from_unit, to_unit_cm)
    converted_to_km = converter.convert(sample_value, from_unit, to_unit_km)
    
    print(f"{sample_value} {from_unit} is equal to {converted_to_cm} {to_unit_cm}")
    print(f"{sample_value} {from_unit} is equal to {converted_to_km} {to_unit_km}")