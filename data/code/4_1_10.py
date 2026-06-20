class DistanceConverter:
    def __init__(self, value, unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if unit not in ("meters", "kilometers", "miles"):
            raise ValueError("Unit must be meters, kilometers, or miles")
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == "meters":
            return self.value
        if self.unit == "kilometers":
            return self.value * 1000
        if self.unit == "miles":
            return self.value * 1609.344

    def to_kilometers(self):
        return self.to_meters() / 1000

    def to_miles(self):
        return self.to_meters() / 1609.344

    def convert(self, target_unit):
        if target_unit == "meters":
            return self.to_meters()
        if target_unit == "kilometers":
            return self.to_kilometers()
        if target_unit == "miles":
            return self.to_miles()

if __name__ == '__main__':
    converter = DistanceConverter(1, "kilometers")
    print(converter.convert("meters"))
    print(converter.convert("miles"))

    converter2 = DistanceConverter(1, "miles")
    print(converter2.convert("kilometers"))
    print(converter2.convert("meters"))

    converter3 = DistanceConverter(1000, "meters")
    print(converter3.convert("kilometers"))
    print(converter3.convert("miles"))