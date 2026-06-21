class Volume:
    CC_TO_LITERS = 1e-3
    CC_TO_MILLILITERS = 1e3
    CC_TO_GALLONS = 2.64172052 * 1e-6
    CC_TO_CUBIC_METERS = 1e-6

    def __init__(self, cubic_centimeters):
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self._convert(Volume.CC_TO_LITERS)

    def to_milliliters(self):
        return self._convert(Volume.CC_TO_MILLILITERS)

    def to_gallons(self):
        return self._convert(Volume.CC_TO_GALLONS)

    def to_cubic_meters(self):
        return self._convert(Volume.CC_TO_CUBIC_METERS)

    def _convert(self, factor):
        return self.cubic_centimeters * factor

if __name__ == '__main__':
    sample_volume = Volume(500)
    print('Liters:', sample_volume.to_liters())
    print('Milliliters:', sample_volume.to_milliliters())
    print('Gallons:', sample_volume.to_gallons())
    print('Cubic Meters:', sample_volume.to_cubic_meters())