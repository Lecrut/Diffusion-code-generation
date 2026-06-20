class LengthConverter:
    METERS = 1.0
    KILOMETERS = 0.001
    CENTIMETERS = 100.0
    MILLIMETERS = 1000.0
    INCHES = 39.37007874015748
    FEET = 3.280839895013123
    YARDS = 1.0936132983377078
    MILES = 0.0006213711922373341

    def __init__(self, value, unit):
        self._meters = value * self.UNIT_FACTORS[unit]

    def to_meters(self):
        return self._meters

    def to(self, target_unit):
        return self._meters / self.UNIT_FACTORS[target_unit]

    @property
    def UNIT_FACTORS(self):
        return {
            "m": self.METERS,
            "km": self.KILOMETERS,
            "cm": self.CENTIMETERS,
            "mm": self.MILLIMETERS,
            "in": self.INCHES,
            "ft": self.FEET,
            "yd": self.YARDS,
            "mi": self.MILES
        }

if __name__ == '__main__':
    converter = LengthConverter(1.0, "km")
    print(converter.to("m"))
    print(converter.to("ft"))
    print(converter.to("mi"))
    print(converter.to("cm"))
    print(converter.to("in"))