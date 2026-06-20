class Volume:
    def __init__(self, value, unit="cm3"):
        self._base_cm3 = self._to_cm3(value, unit)

    def _to_cm3(value, unit):
        conversions = {
            "cm3": 1.0,
            "m3": 1000000.0,
            "liter": 1000.0,
            "ml": 1.0,
            "gallon": 3785.411784
        }
        if unit not in conversions:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * conversions[unit]

    def to_cm3(self):
        return self._base_cm3

    def to_m3(self):
        return self._base_cm3 / 1000000.0

    def to_liter(self):
        return self._base_cm3 / 1000.0

    def to_ml(self):
        return self._base_cm3

    def to_gallon(self):
        return self._base_cm3 / 3785.411784

    def add(self, other):
        new_cm3 = self._base_cm3 + other._base_cm3
        return Volume(new_cm3, "cm3")

    def subtract(self, other):
        new_cm3 = self._base_cm3 - other._base_cm3
        return Volume(new_cm3, "cm3")

    def multiply(self, scalar):
        new_cm3 = self._base_cm3 * scalar
        return Volume(new_cm3, "cm3")

    def divide(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide volume by zero")
        new_cm3 = self._base_cm3 / scalar
        return Volume(new_cm3, "cm3")

    def equals(self, other):
        return self._base_cm3 == other._base_cm3

if __name__ == '__main__':
    v1 = Volume(1000, "ml")
    v2 = Volume(1, "liter")
    v3 = Volume(1000, "cm3")
    
    sum_v = v1.add(v2)
    print(sum_v.to_liter())
    
    diff_v = v1.subtract(v3)
    print(diff_v.to_cm3())
    
    mult_v = v1.multiply(2)
    print(mult_v.to_gallon())
    
    div_v = v1.divide(10)
    print(div_v.to_ml())
    
    print(v1.equals(v2))
    print(v1.equals(v3))