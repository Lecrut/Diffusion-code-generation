class LengthConverter:
    def __init__(self):
        self.meters_to_feet = 3.28084
        self.feet_to_meters = 1 / self.meters_to_feet

    def convert(self, value, from_unit, to_unit):
        if from_unit == "meters" and to_unit == "feet":
            return value * self.meters_to_feet
        elif from_unit == "feet" and to_unit == "meters":
            return value * self.feet_to_meters
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, "meters", "feet")
    print(result1)
    result2 = converter.convert(32.8084, "feet", "meters")
    print(result2)