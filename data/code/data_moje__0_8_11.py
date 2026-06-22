class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == "meters" and to_unit == "feet":
            return value * 3.28084
        elif from_unit == "feet" and to_unit == "meters":
            return value / 3.28084
        else:
            return value

if __name__ == '__main__':
    converter = LengthConverter()
    result = converter.convert(1, "meters", "feet")
    print(result)
    result2 = converter.convert(1, "feet", "meters")
    print(result2)