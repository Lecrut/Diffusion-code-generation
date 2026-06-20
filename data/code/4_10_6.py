class DistanceConverter:
    MILES_TO_KM = 1.60934

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self.value = value

    def to_kilometers(self):
        if self.value < 0:
            raise ValueError("Distance cannot be negative")
        return self.value * self.MILES_TO_KM

    def to_miles(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Kilometers value must be a number")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers / self.MILES_TO_KM

if __name__ == "__main__":
    converter = DistanceConverter(10)
    km_value = converter.to_kilometers()
    miles_value = converter.to_miles(km_value)
    print(km_value)
    print(miles_value)