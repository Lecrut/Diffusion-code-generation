class Volume:
    def __init__(self, cubic_cm):
        self.cubic_cm = cubic_cm

    def to_liters(self):
        return self.cubic_cm / 1000.0

    def to_milliliters(self):
        return self.cubic_cm * 10.0

    def to_gallons(self):
        return self.cubic_cm / 3785.411784

    def to_cubic_meters(self):
        return self.cubic_cm / 1_000_000.0

if __name__ == '__main__':
    sample_volume = Volume(500)
    print("Liters:", sample_volume.to_liters())
    print("Milliliters:", sample_volume.to_milliliters())
    print("Gallons:", sample_volume.to_gallons())
    print("Cubic Meters:", sample_volume.to_cubic_meters())