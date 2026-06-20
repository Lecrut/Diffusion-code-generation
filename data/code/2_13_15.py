class Volume:
    def __init__(self, value, unit="cm3"):
        self._base_value = self._convert_to_cm3(value, unit)

    @staticmethod
    def _convert_to_cm3(value, unit):
        conversions = {
            "cm3": 1.0,
            "ml": 1.0,
            "l": 1000.0,
            "m3": 1000000.0,
            "gal": 3785.411784
        }
        if unit not in conversions:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * conversions[unit]

    def _convert_from_cm3(self, target_unit):
        conversions = {
            "cm3": 1.0,
            "ml": 1.0,
            "l": 1000.0,
            "m3": 1000000.0,
            "gal": 3785.411784
        }
        return self._base_value / conversions[target_unit]

    def to_cm3(self):
        return self._base_value

    def to_ml(self):
        return self._convert_from_cm3("ml")

    def to_l(self):
        return self._convert_from_cm3("l")

    def to_m3(self):
        return self._convert_from_cm3("m3")

    def to_gal(self):
        return self._convert_from_cm3("gal")

    def __add__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only add Volume instances")
        return Volume(self._base_value + other._base_value)

    def __sub__(self, other):
        if not isinstance(other, Volume):
            raise TypeError("Can only subtract Volume instances")
        return Volume(self._base_value - other._base_value)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a number")
        return Volume(self._base_value * scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only divide by a number")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero")
        return Volume(self._base_value / scalar)

    def __repr__(self):
        return f"Volume({self._base_value}, 'cm3')"

    def __eq__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value == other._base_value

    def __ne__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value != other._base_value

    def __lt__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value < other._base_value

    def __le__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value <= other._base_value

    def __gt__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value > other._base_value

    def __ge__(self, other):
        if not isinstance(other, Volume):
            return NotImplemented
        return self._base_value >= other._base_value

if __name__ == "__main__":
    v1 = Volume(1, "l")
    v2 = Volume(500, "ml")
    v3 = v1 + v2
    print(v3.to_ml())
    
    v4 = Volume(1, "m3")
    print(v4.to_l())
    
    v5 = Volume(1000, "cm3")
    v6 = Volume(1, "gal")
    print(v6.to_cm3())
    
    v7 = Volume(10, "cm3") * 2
    print(v7.to_cm3())
    
    v8 = Volume(100, "ml") / 2
    print(v8.to_ml())