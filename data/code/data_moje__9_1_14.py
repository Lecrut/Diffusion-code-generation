class VolumeConverter:
    _LITERS_PER_MILLILITER = 0.001
    _MILLILITERS_PER_LITER = 1000.0
    _CUBIC_INCHES_PER_CUBIC_METER = 61023.74409473228
    _CUBIC_METERS_PER_CUBIC_INCH = 1.0 / 61023.74409473228

    def __init__(self):
        self.conversion_factors = {
            'liters_to_milliliters': self._MILLILITERS_PER_LITER,
            'milliliters_to_liters': self._LITERS_PER_MILLILITER,
            'cubic_meters_to_cubic_inches': self._CUBIC_INCHES_PER_CUBIC_METER,
            'cubic_inches_to_cubic_meters': self._CUBIC_METERS_PER_CUBIC_INCH
        }

    def _apply_factor(self, value, factor_key):
        return value * self.conversion_factors[factor_key]

    def liters_to_milliliters(self, liters):
        return self._apply_factor(liters, 'liters_to_milliliters')

    def milliliters_to_liters(self, milliliters):
        return self._apply_factor(milliliters, 'milliliters_to_liters')

    def cubic_meters_to_cubic_inches(self, cubic_meters):
        return self._apply_factor(cubic_meters, 'cubic_meters_to_cubic_inches')

    def cubic_inches_to_cubic_meters(self, cubic_inches):
        return self._apply_factor(cubic_inches, 'cubic_inches_to_cubic_meters')

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 5.5
    sample_milliliters = 250.0
    sample_cubic_meters = 1.2
    sample_cubic_inches = 1000.0

    print(converter.liters_to_milliliters(sample_liters))
    print(converter.milliliters_to_liters(sample_milliliters))
    print(converter.cubic_meters_to_cubic_inches(sample_cubic_meters))
    print(converter.cubic_inches_to_cubic_meters(sample_cubic_inches))