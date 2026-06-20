class DistanceConverter:
    METERS_TO_KM = 0.001
    METERS_TO_MILES = 0.000621371
    KM_TO_METERS = 1000.0
    KM_TO_MILES = 0.621371
    MILES_TO_METERS = 1609.344
    MILES_TO_KM = 1.609344

    def __init__(self, value, unit):
        if unit not in ("meters", "kilometers", "miles"):
            raise ValueError("Unit must be 'meters', 'kilometers', or 'miles'")
        self.value = float(value)
        self.unit = unit

    def to_meters(self):
        if self.unit == "meters":
            return self.value
        if self.unit == "kilometers":
            return self.value * self.KM_TO_METERS
        return self.value * self.MILES_TO_METERS

    def to_kilometers(self):
        meters = self.to_meters()
        return meters * self.METERS_TO_KM

    def to_miles(self):
        meters = self.to_meters()
        return meters * self.METERS_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter(1, "kilometers")
    print(converter.to_meters())
    print(converter.to_miles())