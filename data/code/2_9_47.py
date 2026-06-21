class Volume:
    def __init__(self, cubic_centimeters):
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self._convert_to_unit(1e-3)

    def to_milliliters(self):
        return self._convert_to_unit(1e3)

    def to_gallons(self):
        return self._convert_to_unit(2.64172052 * 1e-6)

    def to_cubic_meters(self):
        return self._convert_to_unit(1e-6)

    def _convert_to_unit(self, conversion_factor):
        return self.cubic_centimeters * conversion_factor

if __name__ == '__main__':
    sample_volume = Volume(500)
    print('Liters:', sample_volume.to_liters())
    print('Milliliters:', sample_volume.to_milliliters())
    print('Gallons:', sample_volume.to_gallons())
    print('Cubic Meters:', sample_volume.to_cubic_meters())