class Volume:
    BASE_UNIT = "cc"

    CONVERSIONS_TO_CC = {
        "liters": 1000.0,
        "milliliters": 1.0,
        "gallons": 3785.411784,
        "cubic_meters": 1000000.0,
        "cubic_centimeters": 1.0
    }

    def __init__(self, value, unit="cubic_centimeters"):
        if unit not in self.CONVERSIONS_TO_CC:
            raise ValueError("Unsupported unit")
        self._value_cc = value * self.CONVERSIONS_TO_CC[unit]

    def to(self, unit):
        if unit not in self.CONVERSIONS_TO_CC:
            raise ValueError("Unsupported unit")
        return self._value_cc / self.CONVERSIONS_TO_CC[unit]

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self._value_cc + other._value_cc, "cubic_centimeters")
        raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self._value_cc - other._value_cc, "cubic_centimeters")
        raise TypeError("Unsupported operand type")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Volume(self._value_cc * factor, "cubic_centimeters")
        raise TypeError("Unsupported operand type")

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)):
            return Volume(self._value_cc / factor, "cubic_centimeters")
        raise TypeError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, Volume):
            return abs(self._value_cc - other._value_cc) < 1e-9
        return False

    def __repr__(self):
        return f"Volume({self.to('cubic_centimeters')} cc)"

if __name__ == '__main__':
    v1 = Volume(1, "liters")
    v2 = Volume(500, "milliliters")
    v3 = Volume(1, "gallons")

    print(v1.to("milliliters"))
    print(v2.to("liters"))
    print(v3.to("cubic_meters"))

    v_sum = v1 + v2
    print(v_sum.to("milliliters"))

    v_diff = v1 - v2
    print(v_diff.to("cubic_centimeters"))

    v_scaled = v1 * 2.5
    print(v_scaled.to("liters"))

    v_div = v3 / 2
    print(v_div.to("milliliters"))

    print(v1 == Volume(1000, "milliliters"))
    print(v1 == v2)

    print(repr(v1))