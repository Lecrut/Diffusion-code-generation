class Volume:
    LITERS_TO_CC = 1000.0
    MILLILITERS_TO_CC = 0.001
    GALLONS_TO_CC = 3785.411784
    CUBIC_METERS_TO_CC = 1000000.0

    def __init__(self, cubic_centimeters):
        if cubic_centimeters < 0:
            raise ValueError("Volume cannot be negative")
        self.cubic_centimeters = cubic_centimeters

    def to_liters(self):
        return self.cubic_centimeters / self.LITERS_TO_CC

    def to_milliliters(self):
        return self.cubic_centimeters / self.MILLILITERS_TO_CC

    def to_gallons(self):
        return self.cubic_centimeters / self.GALLONS_TO_CC

    def to_cubic_meters(self):
        return self.cubic_centimeters / self.CUBIC_METERS_TO_CC

if __name__ == '__main__':
    sample_volume_cc = 2000
    volume = Volume(sample_volume_cc)
    
    liters = volume.to_liters()
    milliliters = volume.to_milliliters()
    gallons = volume.to_gallons()
    cubic_meters = volume.to_cubic_meters()

    print('Volume in Liters:', liters)
    print('Volume in Milliliters:', milliliters)
    print('Volume in Gallons:', gallons)
    print('Volume in Cubic Meters:', cubic_meters)