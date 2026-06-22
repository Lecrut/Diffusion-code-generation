class Volume:
    def __init__(self, cubic_centimeters=0.0):
        self._cc = float(cubic_centimeters)

    @property
    def cubic_centimeters(self):
        return self._cc

    @cubic_centimeters.setter
    def cubic_centimeters(self, value):
        self._cc = float(value)

    @property
    def liters(self):
        return self._cc / 1000.0

    @liters.setter
    def liters(self, value):
        self._cc = float(value) * 1000.0

    @property
    def milliliters(self):
        return self._cc

    @milliliters.setter
    def milliliters(self, value):
        self._cc = float(value)

    @property
    def gallons(self):
        return self._cc / 3785.411784

    @gallons.setter
    def gallons(self, value):
        self._cc = float(value) * 3785.411784

    @property
    def cubic_meters(self):
        return self._cc / 1000000.0

    @cubic_meters.setter
    def cubic_meters(self, value):
        self._cc = float(value) * 1000000.0

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc + other._cc)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc - other._cc)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Volume(self._cc * float(scalar))
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Volume(self._cc / float(scalar))
        raise ZeroDivisionError("Cannot divide volume by zero")

    def __eq__(self, other):
        if isinstance(other, Volume):
            return abs(self._cc - other._cc) < 1e-9
        return NotImplemented

    def __repr__(self):
        return f"Volume(cubic_centimeters={self._cc})"

if __name__ == '__main__':
    v1 = Volume(liters=1.5)
    print("Volume 1 in liters:", v1.liters)
    print("Volume 1 in milliliters:", v1.milliliters)
    print("Volume 1 in cubic centimeters:", v1.cubic_centimeters)
    print("Volume 1 in gallons:", v1.gallons)
    print("Volume 1 in cubic meters:", v1.cubic_meters)

    v2 = Volume(gallons=0.5)
    print("\nVolume 2 in liters:", v2.liters)
    print("Volume 2 in milliliters:", v2.milliliters)

    v_sum = v1 + v2
    print("\nSum (v1 + v2) in liters:", v_sum.liters)
    print("Sum (v1 + v2) in cubic centimeters:", v_sum.cubic_centimeters)

    v_diff = v1 - v2
    print("\nDifference (v1 - v2) in liters:", v_diff.liters)

    v_scaled = v1 * 2.0
    print("\nScaled (v1 * 2.0) in liters:", v_scaled.liters)

    v_halved = v1 / 2.0
    print("\nHalved (v1 / 2.0) in liters:", v_halved.liters)

    print("\nEquality check (v1 == Volume(liters=1.5)):", v1 == Volume(liters=1.5))
    print("Equality check (v1 == Volume(liters=1.6)):", v1 == Volume(liters=1.6))

    v3 = Volume(cubic_meters=0.001)
    print("\nVolume 3 in cubic centimeters:", v3.cubic_centimeters)
    print("Volume 3 in liters:", v3.liters)