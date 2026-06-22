class Volume:
    def __init__(self, cubic_cm=0.0):
        self._cc = float(cubic_cm)

    @property
    def cubic_cm(self):
        return self._cc

    @property
    def liters(self):
        return self._cc / 1000.0

    @property
    def milliliters(self):
        return self._cc

    @property
    def gallons(self):
        return self._cc / 3785.411784

    @property
    def cubic_meters(self):
        return self._cc / 1000000.0

    def set_from_liters(self, liters):
        self._cc = liters * 1000.0

    def set_from_milliliters(self, ml):
        self._cc = ml

    def set_from_gallons(self, gallons):
        self._cc = gallons * 3785.411784

    def set_from_cubic_meters(self, m3):
        self._cc = m3 * 1000000.0

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc + other._cc)
        raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._cc - other._cc)
        raise TypeError("Unsupported operand type for -")

    def __mul__(self, scalar):
        return Volume(self._cc * scalar)

    def __truediv__(self, scalar):
        return Volume(self._cc / scalar)

    def __eq__(self, other):
        if isinstance(other, Volume):
            return abs(self._cc - other._cc) < 1e-9
        return False

    def __repr__(self):
        return f"Volume(cubic_cm={self._cc})"

if __name__ == '__main__':
    v1 = Volume(1500.0)
    print(v1.liters)
    print(v1.milliliters)
    print(v1.gallons)
    print(v1.cubic_meters)

    v2 = Volume()
    v2.set_from_liters(2.5)
    print(v2.cubic_cm)
    print(v2.milliliters)

    v3 = Volume()
    v3.set_from_gallons(1.0)
    print(v3.liters)
    print(v3.cubic_meters)

    v4 = Volume(100.0)
    v5 = Volume(200.0)
    v_sum = v4 + v5
    print(v_sum.cubic_cm)

    v_diff = v5 - v4
    print(v_diff.cubic_cm)

    v_scaled = v4 * 3.5
    print(v_scaled.liters)

    v_halved = v5 / 2.0
    print(v_halved.milliliters)

    v6 = Volume(500.0)
    v7 = Volume(500.0)
    print(v6 == v7)

    v8 = Volume(500.0)
    v9 = Volume(500.000000001)
    print(v8 == v9)

    v10 = Volume(1000.0)
    v10.set_from_cubic_meters(0.001)
    print(v10.cubic_cm)