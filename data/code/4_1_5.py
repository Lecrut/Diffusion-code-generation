class DistanceConverter:
    FACTORS = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344
    }

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.lower()
        if self.unit not in self.FACTORS:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def _to_base(self):
        return self.value * self.FACTORS[self.unit]

    def to(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in self.FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        base = self._to_base()
        return base / self.FACTORS[target_unit]

    def to_meters(self):
        return self.to('m')

    def to_kilometers(self):
        return self.to('km')

    def to_miles(self):
        return self.to('mi')

if __name__ == '__main__':
    d1 = DistanceConverter(1000, 'm')
    print(d1.to_kilometers())
    print(d1.to_miles())

    d2 = DistanceConverter(1, 'mi')
    print(d2.to_meters())
    print(d2.to_kilometers())

    d3 = DistanceConverter(5, 'km')
    print(d3.to_meters())
    print(d3.to_miles())