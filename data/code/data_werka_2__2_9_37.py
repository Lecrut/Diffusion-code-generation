class Volume:
    LITERS_PER_CC = 1e-3
    MILLILITERS_PER_CC = 1e3
    GALLONS_PER_CC = 2.64172052 * 1e-6
    CUBIC_METERS_PER_CC = 1e-6

    def __init__(self, cubic_centimeters):
        if not isinstance(cubic_centimeters, (int, float)):
            raise TypeError("Volume must be a number")
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self._convert_to_unit(self.LITERS_PER_CC)

    def to_milliliters(self):
        return self._convert_to_unit(self.MILLILITERS_PER_CC)

    def to_gallons(self):
        return self._convert_to_unit(self.GALLONS_PER_CC)

    def to_cubic_meters(self):
        return self._convert_to_unit(self.CUBIC_METERS_PER_CC)

    def _convert_to_unit(self, conversion_factor):
        return self.cubic_centimeters * conversion_factor

if __name__ == '__main__':
    try:
        sample_volume = Volume(500)
        print('Liters:', sample_volume.to_liters())
        print('Milliliters:', sample_volume.to_milliliters())
        print('Gallons:', sample_volume.to_gallons())
        print('Cubic Meters:', sample_volume.to_cubic_meters())
    except (TypeError, ValueError) as e:
        print(e)