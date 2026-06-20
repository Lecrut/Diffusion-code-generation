class Volume:
    LITERS_TO_CC = 1000.0
    MILLILITERS_TO_CC = 1.0
    GALLONS_TO_CC = 3785.411784
    CUBIC_METERS_TO_CC = 1000000.0

    def __init__(self, cc=0.0):
        self.cc = float(cc)

    def __repr__(self):
        return f'Volume(cc={self.cc})'

    def __eq__(self, other):
        if isinstance(other, Volume):
            return abs(self.cc - other.cc) < 1e-09
        return False

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self.cc + other.cc)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self.cc - other.cc)
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Volume(self.cc * factor)
        return NotImplemented

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ZeroDivisionError('Cannot divide volume by zero')
            return Volume(self.cc / divisor)
        return NotImplemented

    def to_liters(self):
        return self.cc / self.LITERS_TO_CC

    def to_milliliters(self):
        return self.cc / self.MILLILITERS_TO_CC

    def to_gallons(self):
        return self.cc / self.GALLONS_TO_CC

    def to_cubic_meters(self):
        return self.cc / self.CUBIC_METERS_TO_CC

    @classmethod
    def from_liters(cls, liters):
        return cls(liters * cls.LITERS_TO_CC)

    @classmethod
    def from_milliliters(cls, milliliters):
        return cls(milliliters * cls.MILLILITERS_TO_CC)

    @classmethod
    def from_gallons(cls, gallons):
        return cls(gallons * cls.GALLONS_TO_CC)

    @classmethod
    def from_cubic_meters(cls, cubic_meters):
        return cls(cubic_meters * cls.CUBIC_METERS_TO_CC)
if __name__ == '__main__':
    v1 = Volume.from_liters(1.5)
    v2 = Volume.from_milliliters(500.0)
    v3 = Volume.from_gallons(1.0)
    v4 = Volume.from_cubic_meters(0.001)
    print(f'Volume 1 (1.5 liters): {v1.to_liters()} liters')
    print(f'Volume 1 (1.5 liters): {v1.to_milliliters()} milliliters')
    print(f'Volume 1 (1.5 liters): {v1.to_gallons()} gallons')
    print(f'Volume 1 (1.5 liters): {v1.to_cubic_meters()} cubic meters')
    print(f'Volume 2 (500 ml): {v2.to_liters()} liters')
    print(f'Volume 2 (500 ml): {v2.to_gallons()} gallons')
    print(f'Volume 3 (1 gallon): {v3.to_liters()} liters')
    print(f'Volume 3 (1 gallon): {v3.to_milliliters()} milliliters')
    print(f'Volume 4 (0.001 m3): {v4.to_liters()} liters')
    v_sum = v1 + v2
    print(f'Sum of v1 and v2: {v_sum.to_liters()} liters')
    v_diff = v3 - v4
    print(f'Difference of v3 and v4: {v_diff.to_liters()} liters')
    v_scaled = v1 * 2.5
    print(f'v1 scaled by 2.5: {v_scaled.to_liters()} liters')
    v_divided = v1 / 3.0
    print(f'v1 divided by 3: {v_divided.to_milliliters()} milliliters')