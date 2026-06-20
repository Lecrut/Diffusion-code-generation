class Volume:
    def __init__(self, value, unit='cm3'):
        self._cc = self._to_cm3(value, unit)

    @staticmethod
    def _to_cm3(value, unit):
        if unit == 'cm3':
            return float(value)
        if unit == 'mL':
            return float(value)
        if unit == 'L':
            return float(value) * 1000.0
        if unit == 'gal':
            return float(value) * 3785.411784
        if unit == 'm3':
            return float(value) * 1000000.0
        raise ValueError("Unsupported unit")

    def to_cm3(self):
        return self._cc

    def to_mL(self):
        return self._cc

    def to_L(self):
        return self._cc / 1000.0

    def to_gal(self):
        return self._cc / 3785.411784

    def to_m3(self):
        return self._cc / 1000000.0

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc + other._cc, 'cm3')
        return Volume(self._cc + float(other), 'cm3')

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc - other._cc, 'cm3')
        return Volume(self._cc - float(other), 'cm3')

    def __mul__(self, other):
        if isinstance(other, Volume):
            raise TypeError("Cannot multiply two Volume objects")
        return Volume(self._cc * float(other), 'cm3')

    def __truediv__(self, other):
        if isinstance(other, Volume):
            if other._cc == 0:
                raise ZeroDivisionError("Cannot divide by zero volume")
            return self._cc / other._cc
        if float(other) == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Volume(self._cc / float(other), 'cm3')

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self._cc == other._cc
        return self._cc == float(other)

    def __repr__(self):
        return f"Volume({self._cc} cm3)"

if __name__ == '__main__':
    v1 = Volume(1, 'L')
    v2 = Volume(1000, 'mL')
    v3 = v1 + v2
    print(v3.to_L())
    v4 = Volume(1, 'gal')
    print(v4.to_L())
    v5 = Volume(1000000, 'cm3')
    print(v5.to_m3())
    v6 = Volume(1, 'm3')
    print(v6.to_gal())
    v7 = Volume(500, 'mL') * 2
    print(v7.to_mL())
    v8 = Volume(10, 'L') / Volume(2, 'L')
    print(v8)
    v9 = Volume(1, 'cm3') == Volume(1, 'mL')
    print(v9)
    v10 = Volume(1, 'm3') - Volume(1000, 'L')
    print(v10.to_cm3())