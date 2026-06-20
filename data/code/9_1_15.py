class VolumeConverter:
    FACTOR_L_TO_ML = 1000.0
    FACTOR_CM_TO_CI = 61023.7440947353
    _VALID_TYPES = (int, float)

    def _validate_numeric(self, value, name):
        if not isinstance(value, self._VALID_TYPES):
            raise TypeError("Value must be numeric")
        if value < 0:
            raise ValueError("Volume cannot be negative")

    def liters_to_milliliters(self, liters):
        self._validate_numeric(liters, "liters")
        return liters * self.FACTOR_L_TO_ML

    def milliliters_to_liters(self, milliliters):
        self._validate_numeric(milliliters, "milliliters")
        return milliliters / self.FACTOR_L_TO_ML

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        self._validate_numeric(cubic_meters, "cubic_meters")
        return cubic_meters * self.FACTOR_CM_TO_CI

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        self._validate_numeric(cubic_inches, "cubic_inches")
        return cubic_inches / self.FACTOR_CM_TO_CI

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(2.5))
    print(converter.milliliters_to_liters(500.0))
    print(converter.cubic_meters_to_cubic_inches(1.0))
    print(converter.cubic_inches_to_cubic_meters(100.0))