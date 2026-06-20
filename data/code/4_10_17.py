class DistanceConverter:
    MILES_TO_KILOMETERS = 1.609344
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self, value, unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type.")
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        if unit not in ("miles", "km", "kilometers", "kilometres"):
            raise ValueError("Unit must be 'miles' or 'km'.")
        self.value = value
        self.unit = unit.lower()

    def to_miles(self):
        if self.unit == "miles":
            return self.value
        return self.value * self.KILOMETERS_TO_MILES

    def to_kilometers(self):
        if self.unit == "km" or self.unit == "kilometers" or self.unit == "kilometres":
            return self.value
        return self.value * self.MILES_TO_KILOMETERS

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit == "miles":
            return self.to_miles()
        if target_unit in ("km", "kilometers", "kilometres"):
            return self.to_kilometers()
        raise ValueError("Target unit must be 'miles' or 'km'.")

if __name__ == '__main__':
    converter = DistanceConverter(5, "miles")
    result_km = converter.convert("km")
    print(result_km)

    converter2 = DistanceConverter(10, "km")
    result_miles = converter2.convert("miles")
    print(result_miles)