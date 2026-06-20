class DistanceConverter:
    MILES = 1.0
    KILOMETERS = 1.60934
    METERS = 1609.34

    def __init__(self, distance=0, unit='miles'):
        if unit not in ('miles', 'kilometers', 'meters'):
            raise ValueError("Unsupported unit. Use 'miles', 'kilometers', or 'meters'.")
        self.distance = distance
        self.unit = unit

    def to_miles(self):
        if self.unit == 'miles':
            return self.distance
        elif self.unit == 'kilometers':
            return self.distance / self.KILOMETERS
        elif self.unit == 'meters':
            return self.distance / self.METERS

    def to_kilometers(self):
        if self.unit == 'miles':
            return self.distance * self.KILOMETERS
        elif self.unit == 'kilometers':
            return self.distance
        elif self.unit == 'meters':
            return self.distance / (self.METERS / self.KILOMETERS)

    def to_meters(self):
        if self.unit == 'miles':
            return self.distance * self.METERS
        elif self.unit == 'kilometers':
            return self.distance * (self.METERS / self.KILOMETERS)
        elif self.unit == 'meters':
            return self.distance

    def convert(self, target_unit):
        if target_unit == 'miles':
            return self.to_miles()
        elif target_unit == 'kilometers':
            return self.to_kilometers()
        elif target_unit == 'meters':
            return self.to_meters()
        else:
            raise ValueError("Unsupported target unit. Use 'miles', 'kilometers', or 'meters'.")

if __name__ == '__main__':
    d1 = DistanceConverter(10, 'miles')
    print(d1.convert('kilometers'))
    print(d1.convert('meters'))

    d2 = DistanceConverter(5, 'kilometers')
    print(d2.convert('miles'))
    print(d2.convert('meters'))

    d3 = DistanceConverter(1000, 'meters')
    print(d3.convert('miles'))
    print(d3.convert('kilometers'))