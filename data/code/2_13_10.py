class Volume:
    def __init__(self, value, unit="cm3"):
        if unit == "cm3":
            self.value = value
        elif unit == "ml":
            self.value = value
        elif unit == "l":
            self.value = value * 1000
        elif unit == "gallon":
            self.value = value * 3785.411784
        elif unit == "m3":
            self.value = value * 1000000
        else:
            raise ValueError("Unsupported unit")

    def to_cm3(self):
        return self.value

    def to_ml(self):
        return self.value

    def to_l(self):
        return self.value / 1000

    def to_gallon(self):
        return self.value / 3785.411784

    def to_m3(self):
        return self.value / 1000000

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self.value + other.value, "cm3")
        raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self.value - other.value, "cm3")
        raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Volume(self.value * other, "cm3")
        raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Volume(self.value / other, "cm3")
        if isinstance(other, Volume):
            return self.value / other.value
        raise TypeError("Unsupported operand type")

    def __repr__(self):
        return f"Volume({self.value} cm3)"

if __name__ == "__main__":
    v1 = Volume(1, "l")
    v2 = Volume(1, "gallon")
    v3 = Volume(1, "m3")
    print(v1.to_ml())
    print(v2.to_l())
    print(v3.to_cm3())
    print((v1 + v2).to_gallon())
    print((v3 - v1).to_m3())