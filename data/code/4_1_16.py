class DistanceConverter:
    METERS_PER_KILOMETER = 1000
    METERS_PER_MILE = 1609.34

    def __init__(self, value, unit):
        if unit not in ["m", "km", "mi"]:
            raise ValueError("Unit must be 'm', 'km', or 'mi'")
        self.meters = value * self.METERS_PER_KILOMETER if unit == "km" else value * self.METERS_PER_MILE if unit == "mi" else value

    def to_meters(self):
        return self.meters

    def to_kilometers(self):
        return self.meters / self.METERS_PER_KILOMETER

    def to_miles(self):
        return self.meters / self.METERS_PER_MILE

if __name__ == '__main__':
    converter = DistanceConverter(5, "km")
    print(converter.to_miles())
    print(converter.to_meters())
    converter_miles = DistanceConverter(3, "mi")
    print(converter_miles.to_kilometers())