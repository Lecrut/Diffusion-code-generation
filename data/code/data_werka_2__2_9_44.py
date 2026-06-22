class Volume:
    LITERS_PER_CC = 1e-3
    MILLILITERS_PER_CC = 1e3
    GALLONS_PER_CC = 2.64172052 * 1e-6
    CUBIC_METERS_PER_CC = 1e-6

    def __init__(self, cubic_centimeters):
        self._validate_volume(cubic_centimeters)
        self.cubic_centimeters = cubic_centimeters

    def _validate_volume(self, volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        if volume < 0:
            raise ValueError("Volume cannot be negative")

    def to_liters(self):
        return self.cubic_centimeters * self.LITERS_PER_CC

    def to_milliliters(self):
        return self.cubic_centimeters * self.MILLILITERS_PER_CC

    def to_gallons(self):
        return self.cubic_centimeters * self.GALLONS_PER_CC

    def to_cubic_meters(self):
        return self.cubic_centimeters * self.CUBIC_METERS_PER_CC

if __name__ == '__main__':
    sample_volume = Volume(1000)
    print('Liters:', sample_volume.to_liters())
    print('Milliliters:', sample_volume.to_milliliters())
    print('Gallons:', sample_volume.to_gallons())
    print('Cubic Meters:', sample_volume.to_cubic_meters())