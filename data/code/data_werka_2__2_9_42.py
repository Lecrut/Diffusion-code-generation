class Volume:
    LITERS_PER_CC = 0.001
    MILLILITERS_PER_CC = 1000
    GALLONS_PER_CC = 0.000264172
    CUBIC_METERS_PER_CC = 0.000001

    def __init__(self, cubic_centimeters):
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self.cubic_centimeters * self.LITERS_PER_CC

    def to_milliliters(self):
        return self.cubic_centimeters * self.MILLILITERS_PER_CC

    def to_gallons(self):
        return self.cubic_centimeters * self.GALLONS_PER_CC

    def to_cubic_meters(self):
        return self.cubic_centimeters * self.CUBIC_METERS_PER_CC

if __name__ == '__main__':
    sample_volume = Volume(1500)
    print('Liters:', sample_volume.to_liters())
    print('Milliliters:', sample_volume.to_milliliters())
    print('Gallons:', sample_volume.to_gallons())
    print('Cubic Meters:', sample_volume.to_cubic_meters())