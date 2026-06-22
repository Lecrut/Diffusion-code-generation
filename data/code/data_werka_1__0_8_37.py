class LengthConverter:
    METER_TO_FEET = 3.28084
    FEET_TO_METER = 1 / 3.28084

    def convert(self, value, from_unit, to_unit):
        if from_unit == "meters" and to_unit == "feet":
            return value * self.METER_TO_FEET
        elif from_unit == "feet" and to_unit == "meters":
            return value * self.FEET_TO_METER
        else:
            raise ValueError("Unsupported unit conversion. Use 'meters' or 'feet'.")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(1, "meters", "feet")
    print(result1)
    result2 = converter.convert(1, "feet", "meters")
    print(result2)