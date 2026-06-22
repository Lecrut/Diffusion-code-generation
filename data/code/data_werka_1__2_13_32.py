class VolumeMeasurements:
    def __init__(self, cubic_centimeters):
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self.cubic_centimeters / 1000.0

    def to_milliliters(self):
        return self.cubic_centimeters * 1000.0

    def to_gallons(self):
        return self.cubic_centimeters * 264.172052 / 1000000.0

    def to_cubic_meters(self):
        return self.cubic_centimeters / 1000000.0

if __name__ == '__main__':
    sample_volume = VolumeMeasurements(500)
    print("Liters:", sample_volume.to_liters())
    print("Milliliters:", sample_volume.to_milliliters())
    print("Gallons:", sample_volume.to_gallons())
    print("Cubic Meters:", sample_volume.to_cubic_meters())