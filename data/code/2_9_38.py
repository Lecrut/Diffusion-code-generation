class Volume:
    def __init__(self, cubic_centimeters):
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self.cubic_centimeters / 1000.0

    def to_milliliters(self):
        return self.cubic_centimeters * 1000.0

    def to_gallons(self):
        return self.cubic_centimeters / 3785.411784

    def to_cubic_meters(self):
        return self.cubic_centimeters / 1_000_000.0

if __name__ == '__main__':
    volume = Volume(1500)
    print("Liters:", volume.to_liters())
    print("Milliliters:", volume.to_milliliters())
    print("Gallons:", volume.to_gallons())
    print("Cubic Meters:", volume.to_cubic_meters())