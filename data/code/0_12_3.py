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
    meters_to_feet = 10
    feet_to_meters = 32.8084
    result1 = converter.convert(meters_to_feet, "meters", "feet")
    print(f"{meters_to_feet} meters is equal to {result1} feet")
    result2 = converter.convert(feet_to_meters, "feet", "meters")
    print(f"{feet_to_meters} feet is equal to {result2} meters")
    result3 = converter.convert(5, "meters", "meters")
    print(f"5 meters is equal to {result3} meters")