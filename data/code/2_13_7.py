class Volume:
    def __init__(self, value, unit='cm3'):
        factors = {
            'cm3': 1.0,
            'm3': 1000000.0,
            'ml': 1.0,
            'l': 1000.0,
            'gal': 3785.411784
        }
        if unit not in factors:
            raise ValueError(f"Unsupported unit: {unit}")
        self.cm3 = value * factors[unit]

    def to_cm3(self):
        return self.cm3

    def to_m3(self):
        return self.cm3 / 1000000.0

    def to_ml(self):
        return self.cm3

    def to_l(self):
        return self.cm3 / 1000.0

    def to_gal(self):
        return self.cm3 / 3785.411784

    def _add(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only add Volume instances")
        return Volume(self.cm3 + other.cm3, 'cm3')

    def _sub(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only subtract Volume instances")
        return Volume(self.cm3 - other.cm3, 'cm3')

    def _mul(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        return Volume(self.cm3 * scalar, 'cm3')

    def _div(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero")
        return Volume(self.cm3 / scalar, 'cm3')

    def __add__(self, other):
        return self._add(other)

    def __sub__(self, other):
        return self._sub(other)

    def __mul__(self, scalar):
        return self._mul(scalar)

    def __rmul__(self, scalar):
        return self._mul(scalar)

    def __truediv__(self, scalar):
        return self._div(scalar)

    def __eq__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self.cm3 == other.cm3

    def __repr__(self):
        return f"Volume({self.cm3} cm3)"

if __name__ == '__main__':
    v1 = Volume(1, 'l')
    v2 = Volume(1000, 'ml')
    v3 = v1 + v2
    print(v3.to_l())
    print(v1.to_gal())