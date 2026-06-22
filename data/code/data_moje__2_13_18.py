class Volume:
    def __init__(self, cubic_centimeters):
        self.cubic_centimeters = float(cubic_centimeters)

    def to_liters(self):
        return self.cubic_centimeters / 1000.0

    def to_milliliters(self):
        return self.cubic_centimeters

    def to_gallons(self):
        return self.cubic_centimeters / 3785.411784

    def to_cubic_meters(self):
        return self.cubic_centimeters / 1000000.0

    def __str__(self):
        return f"{self.cubic_centimeters} cm³"

if __name__ == '__main__':
    sample_volume = Volume(5000)
    print(sample_volume.to_liters())
    print(sample_volume.to_milliliters())
    print(sample_volume.to_gallons())
    print(sample_volume.to_cubic_meters())