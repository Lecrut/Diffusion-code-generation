class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == 'meters':
            return self.value
        if self.unit == 'kilometers':
            return self.value * 1000
        if self.unit == 'miles':
            return self.value * 1609.34
        raise ValueError(f"Unknown unit: {self.unit}")

    def to_kilometers(self):
        meters = self.to_meters()
        return meters / 1000

    def to_miles(self):
        meters = self.to_meters()
        return meters / 1609.34

    def convert(self, target_unit):
        if self.unit == target_unit:
            return self.value
        if target_unit == 'meters':
            return self.to_meters()
        if target_unit == 'kilometers':
            return self.to_kilometers()
        if target_unit == 'miles':
            return self.to_miles()
        raise ValueError(f"Unknown target unit: {target_unit}")

    def add(self, other):
        if not isinstance(other, DistanceConverter):
            raise TypeError("Can only add DistanceConverter instances")
        meters = self.to_meters() + other.to_meters()
        return DistanceConverter(meters, 'meters')

    def subtract(self, other):
        if not isinstance(other, DistanceConverter):
            raise TypeError("Can only subtract DistanceConverter instances")
        meters = self.to_meters() - other.to_meters()
        return DistanceConverter(meters, 'meters')

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __repr__(self):
        return f"DistanceConverter({self.value}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, DistanceConverter):
            return False
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() >= other.to_meters()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

if __name__ == '__main__':
    d1 = DistanceConverter(5, 'kilometers')
    d2 = DistanceConverter(3, 'miles')

    print(d1.convert('meters'))
    print(d2.convert('kilometers'))

    d3 = d1.add(d2)
    print(d3.convert('miles'))

    d4 = DistanceConverter(1000, 'meters')
    d5 = DistanceConverter(1, 'kilometers')
    print(d4 == d5)

    d6 = DistanceConverter(100, 'meters')
    d7 = DistanceConverter(150, 'meters')
    print(d6 < d7)

    d8 = d7.subtract(d6)
    print(d8.value)