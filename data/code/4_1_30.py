class DistanceConverter:
    def __init__(self, distance, unit):
        self.distance = distance
        self.unit = unit.lower()

    def to_meters(self):
        if self.unit == 'meters':
            return self.distance
        elif self.unit == 'kilometers':
            return self.distance * 1000
        elif self.unit == 'miles':
            return self.distance * 1609.34

    def to_kilometers(self):
        if self.unit == 'meters':
            return self.distance / 1000
        elif self.unit == 'kilometers':
            return self.distance
        elif self.unit == 'miles':
            return self.distance * 1.60934

    def to_miles(self):
        if self.unit == 'meters':
            return self.distance / 1609.34
        elif self.unit == 'kilometers':
            return self.distance / 1.60934
        elif self.unit == 'miles':
            return self.distance

if __name__ == '__main__':
    converter = DistanceConverter(5, 'kilometers')
    print(f"5 kilometers in meters: {converter.to_meters()}")
    print(f"5 kilometers in kilometers: {converter.to_kilometers()}")
    print(f"5 kilometers in miles: {converter.to_miles()}")

    converter = DistanceConverter(10, 'miles')
    print(f"10 miles in meters: {converter.to_meters()}")
    print(f"10 miles in kilometers: {converter.to_kilometers()}")
    print(f"10 miles in miles: {converter.to_miles()}")

    converter = DistanceConverter(2000, 'meters')
    print(f"2000 meters in meters: {converter.to_meters()}")
    print(f"2000 meters in kilometers: {converter.to_kilometers()}")
    print(f"2000 meters in miles: {converter.to_miles()}")