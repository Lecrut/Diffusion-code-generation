class DistanceConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        if self.unit == 'meters':
            return self.value
        elif self.unit == 'kilometers':
            return self.value * 1000
        elif self.unit == 'miles':
            return self.value * 1609.344
        else:
            raise ValueError(f"Unknown unit: {self.unit}")

    def to_kilometers(self):
        meters = self.to_meters()
        return meters / 1000

    def to_miles(self):
        meters = self.to_meters()
        return meters / 1609.344

    def convert(self, target_unit):
        if target_unit == 'meters':
            return (self.to_meters(), 'meters')
        elif target_unit == 'kilometers':
            return (self.to_kilometers(), 'kilometers')
        elif target_unit == 'miles':
            return (self.to_miles(), 'miles')
        else:
            raise ValueError(f"Unknown target unit: {target_unit}")

    def __repr__(self):
        return f"DistanceConverter(value={self.value}, unit='{self.unit}')"

    def __add__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        result_meters = self.to_meters() + other.to_meters()
        return DistanceConverter(result_meters, 'meters')

    def __sub__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        result_meters = self.to_meters() - other.to_meters()
        return DistanceConverter(result_meters, 'meters')

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            result_value = self.value * factor
            return DistanceConverter(result_value, self.unit)
        return NotImplemented

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            result_value = self.value / divisor
            return DistanceConverter(result_value, self.unit)
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __gt__(self, other):
        if not isinstance(other, DistanceConverter):
            return NotImplemented
        return self.to_meters() > other.to_meters()

if __name__ == '__main__':
    d1 = DistanceConverter(1, 'kilometers')
    result_km = d1.to_kilometers()
    result_mi = d1.to_miles()
    result_m = d1.to_meters()
    
    d2 = DistanceConverter(0.621371, 'miles')
    d3 = DistanceConverter(1, 'kilometers')
    
    sum_dist = d2 + d3
    sum_in_miles = sum_dist.to_miles()
    
    print(f"{d1} to kilometers: {result_km}")
    print(f"{d1} to miles: {result_mi}")
    print(f"{d1} to meters: {result_m}")
    print(f"{d2} == {d3}: {d2 == d3}")
    print(f"{d2} > {d3}: {d2 > d3}")
    print(f"Sum of {d2} and {d3} in miles: {sum_in_miles}")