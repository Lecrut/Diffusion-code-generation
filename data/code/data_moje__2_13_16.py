class Volume:
    def __init__(self, cc_value=0.0):
        self._cc = float(cc_value)

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
        elif isinstance(other, (int, float)):
            return Volume(self._cc + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc - other._cc)
        elif isinstance(other, (int, float)):
            return Volume(self._cc - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Volume(self._cc * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Volume(self._cc / other)
        if isinstance(other, Volume) and other._cc != 0:
            return self._cc / other._cc
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Volume):
            return abs(self._cc - other._cc) < 1e-9
        return NotImplemented

    def __repr__(self):
        return f"Volume(cc={self._cc})"

    def __str__(self):
        return f"{self._cc} cm³"

if __name__ == '__main__':
    v1 = Volume(cc_value=1000)
    v2 = Volume()
    v2.liters = 1.5

    print(v1)
    print(v1.liters)
    print(v1.milliliters)
    print(v1.gallons)
    print(v1.cubic_meters)

    print(v2)
    print(v2.cubic_centimeters)

    v3 = v1 + v2
    print(v3)
    print(v3.liters)

    v4 = v3 * 2.0
    print(v4)
    print(v4.milliliters)

    v5 = v4 / 2.0
    print(v5)
    print(v5 == v3)

    v6 = Volume()
    v6.gallons = 1.0
    print(v6)
    print(v6.liters)

    v7 = Volume()
    v7.cubic_meters = 0.001
    print(v7)
    print(v7.liters)