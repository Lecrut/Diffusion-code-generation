class DistanceConverter:

    def __init__(self, meters):
        self.meters = meters

    def to_kilometers(self):
        return self.meters / 1000.0

    def to_miles(self):
        return self.meters * 0.000621371

    def from_kilometers(self, kilometers):
        self.meters = kilometers * 1000.0
        return self

    def from_miles(self, miles):
        self.meters = miles / 0.000621371
        return self
if __name__ == '__main__':
    converter = DistanceConverter(1000)
    print(converter.to_kilometers())
    print(converter.to_miles())
    converter.from_kilometers(5.0)
    print(converter.meters)
    converter.from_miles(10.0)
    print(converter.meters)