class VolumeConverter:
    BASE_UNIT = "liters"

    TO_BASE = {
        "liters": 1.0,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.24,
        "fluid_ounces": 0.0295735,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
        "cubic_meters": 1000.0,
        "cubic_centimeters": 0.001,
        "cubic_inches": 0.0163871,
        "cubic_feet": 28.3168,
    }

    def __init__(self):
        self.supported_units = list(self.TO_BASE.keys())

    def to_base(self, value, unit):
        unit = unit.lower()
        if unit not in self.TO_BASE:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.TO_BASE[unit]

    def from_base(self, base_value, unit):
        unit = unit.lower()
        if unit not in self.TO_BASE:
            raise ValueError(f"Unsupported unit: {unit}")
        return base_value / self.TO_BASE[unit]

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

    def get_supported_units(self):
        return self.supported_units

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, "gallons", "liters"))
    print(converter.convert(1, "liters", "milliliters"))
    print(converter.convert(500, "milliliters", "cups"))
    print(converter.to_base(1, "gallons"))
    print(converter.from_base(1, "gallons"))
    print(converter.get_supported_units())