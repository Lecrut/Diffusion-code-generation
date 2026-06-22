class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters = 0.0
        if from_unit == "meters":
            meters = value
        elif from_unit == "feet":
            meters = value / 3.28084
        else:
            raise ValueError(f"Unknown source unit: {from_unit}")

        result = 0.0
        if to_unit == "meters":
            result = meters
        elif to_unit == "feet":
            result = meters * 3.28084
        else:
            raise ValueError(f"Unknown target unit: {to_unit}")

        return result

if __name__ == '__main__':
    converter = LengthConverter()
    converted_value = converter.convert(100, "meters", "feet")
    print(converted_value)