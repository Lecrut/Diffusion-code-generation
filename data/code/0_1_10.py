class UnitConverter:
    FEET_PER_METER = 3.28084
    METERS_PER_KILOMETER = 1000.0
    METERS_PER_FOOT = 1.0 / FEET_PER_METER
    KILOMETERS_PER_METER = 1.0 / METERS_PER_KILOMETER

    def __init__(self, value, source_unit):
        self.value = value
        self.source_unit = source_unit.lower()
        self.meters = self._to_meters()

    def _to_meters(self):
        if self.source_unit == 'meters':
            return self.value
        elif self.source_unit == 'feet':
            return self.value * self.METERS_PER_FOOT
        elif self.source_unit == 'kilometers':
            return self.value * self.METERS_PER_KILOMETER
        else:
            raise ValueError("Unsupported unit")

    def to_feet(self):
        return self.meters * self.FEET_PER_METER

    def to_kilometers(self):
        return self.meters * self.KILOMETERS_PER_METER

    def to_meters(self):
        return self.meters

if __name__ == '__main__':
    converter = UnitConverter(100, 'meters')
    print(converter.to_feet())
    print(converter.to_kilometers())
    print(converter.to_meters())

    converter2 = UnitConverter(1, 'kilometers')
    print(converter2.to_feet())
    print(converter2.to_meters())

    converter3 = UnitConverter(10, 'feet')
    print(converter3.to_kilometers())
    print(converter3.to_meters())