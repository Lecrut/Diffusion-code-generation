class LengthConverter:
    METERS_PER_UNIT = {
        "meter": 1.0,
        "m": 1.0,
        "kilometer": 1000.0,
        "km": 1000.0,
        "centimeter": 0.01,
        "cm": 0.01,
        "millimeter": 0.001,
        "mm": 0.001,
        "inch": 0.0254,
        "in": 0.0254,
        "foot": 0.3048,
        "ft": 0.3048,
        "yard": 0.9144,
        "yd": 0.9144,
        "mile": 1609.344,
        "mi": 1609.344,
    }

    def convert(self, value, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        if from_unit_lower not in self.METERS_PER_UNIT:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit_lower not in self.METERS_PER_UNIT:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        meters = value * self.METERS_PER_UNIT[from_unit_lower]
        result = meters / self.METERS_PER_UNIT[to_unit_lower]
        return result

if __name__ == "__main__":
    converter = LengthConverter()
    result = converter.convert(10, "mile", "kilometer")
    print(result)
    result = converter.convert(100, "centimeter", "inch")
    print(result)
    result = converter.convert(5, "ft", "m")
    print(result)