class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.conversion_factors = {}

    def add_conversion_factor(self, target_unit, factor):
        self.conversion_factors[target_unit] = factor

    def convert(self, value, from_unit):
        if from_unit == self.base_unit:
            return value
        elif from_unit in self.conversion_factors:
            return value * self.conversion_factors[from_unit]
        else:
            raise ValueError(f"Conversion from {from_unit} to {self.base_unit} is not supported.")

if __name__ == '__main__':
    converter = UnitConverter('meters')
    converter.add_conversion_factor('centimeters', 100)
    converter.add_conversion_factor('kilometers', 0.001)

    value_cm = 250
    from_unit_cm = 'centimeters'
    converted_value_m = converter.convert(value_cm, from_unit_cm)
    print(f"{value_cm} {from_unit_cm} is equal to {converted_value_m} meters")

    value_km = 5
    from_unit_km = 'kilometers'
    converted_value_m_km = converter.convert(value_km, from_unit_km)
    print(f"{value_km} {from_unit_km} is equal to {converted_value_m_km} meters")