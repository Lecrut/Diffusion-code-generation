class UnitConverter:
    FEET_PER_METER = 3.280839895
    METERS_PER_FOOT = 0.3048
    KILOMETERS_PER_METER = 0.001
    METERS_PER_KILOMETER = 1000.0
    FEET_PER_KILOMETER = FEET_PER_METER * METERS_PER_KILOMETER
    KILOMETERS_PER_FOOT = METERS_PER_FOOT * KILOMETERS_PER_METER

    def __init__(self):
        self._cache = {}

    def _get_or_compute(self, key, func):
        if key not in self._cache:
            self._cache[key] = func()
        return self._cache[key]

    def meters_to_feet(self, meters):
        return meters * self.FEET_PER_METER

    def feet_to_meters(self, feet):
        return feet * self.METERS_PER_FOOT

    def meters_to_kilometers(self, meters):
        return meters * self.KILOMETERS_PER_METER

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.METERS_PER_KILOMETER

    def feet_to_kilometers(self, feet):
        return feet * self.KILOMETERS_PER_FOOT

    def kilometers_to_feet(self, kilometers):
        return kilometers * self.FEET_PER_KILOMETER

    def convert(self, from_unit, to_unit, value):
        conversions = {
            ('meters', 'feet'): self.meters_to_feet,
            ('feet', 'meters'): self.feet_to_meters,
            ('meters', 'kilometers'): self.meters_to_kilometers,
            ('kilometers', 'meters'): self.kilometers_to_meters,
            ('feet', 'kilometers'): self.feet_to_kilometers,
            ('kilometers', 'feet'): self.kilometers_to_feet,
            ('meters', 'meters'): lambda x: x,
            ('feet', 'feet'): lambda x: x,
            ('kilometers', 'kilometers'): lambda x: x,
        }
        func = conversions.get((from_unit, to_unit))
        if func is None:
            raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
        return func(value)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(100))
    print(converter.feet_to_meters(328.0839895))
    print(converter.meters_to_kilometers(1500))
    print(converter.kilometers_to_meters(2.5))
    print(converter.convert('meters', 'kilometers', 500))
    print(converter.convert('feet', 'kilometers', 3280.839895))