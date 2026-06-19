class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == "meters" and to_unit == "feet":
            return value * 3.28084
        elif from_unit == "feet" and to_unit == "meters":
            return value / 3.28084
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(1, "meters", "feet")
    print(result1)
    result2 = converter.convert(10, "feet", "meters")
    print(result2)