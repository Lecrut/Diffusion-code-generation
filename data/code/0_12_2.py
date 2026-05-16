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
    meters = 10
    feet = 32.8084
    result1 = converter.convert(meters, "meters", "feet")
    print(f"{meters} meters is equal to {result1} feet")
    result2 = converter.convert(feet, "feet", "meters")
    print(f"{feet} feet is equal to {result2} meters")
    result3 = converter.convert(5, "meters", "meters")
    print(f"5 meters is equal to {result3} meters")
    result4 = converter.convert(100, "feet", "meters")
    print(f"100 feet is equal to {result4} meters")