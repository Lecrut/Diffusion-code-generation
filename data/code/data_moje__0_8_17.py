class LengthConverter:
    METER_TO_FEET = 3.28084
    FEET_TO_METER = 0.3048

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "meters" and to_unit == "feet":
            return value * self.METER_TO_FEET
        if from_unit == "feet" and to_unit == "meters":
            return value * self.FEET_TO_METER
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, "meters", "feet"))
    print(converter.convert(1, "feet", "meters"))
    print(converter.convert(100, "meters", "feet"))
    print(converter.convert(100, "feet", "meters"))